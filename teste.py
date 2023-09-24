import gradio as gr
import shared
import modules.html
import modules.flags as flags
from modules.sdxl_styles import style_keys,aspect_ratios,fooocus_expansion, default_styles


shared.gradio_root = gr.Blocks(title='Fooocus', css=modules.html.css).queue()

def click(a):
    return a


# Lança o aplicativo Gradio
with shared.gradio_root:
    with gr.Row():
        with gr.Column():
            gallery = gr.Gallery(label='Gallery', show_label=False, object_fit='contain', height=720, visible=True)
            with gr.Row(elem_classes='type_row'):
                with gr.Column(scale=0.85):
                    prompt = gr.Textbox(show_label=False, placeholder="Type prompt here.", container=False, autofocus=True, elem_classes='type_row', lines=1024)
                with gr.Column(scale=0.15, min_width=0):
                    run_button = gr.Button(label="Generate", value="Generate", elem_classes='type_row', visible=True)
            with gr.Row(elem_classes='advanced_check_row'):
                advanced_checkbox = gr.Checkbox(label='Advanced', value=False, container=False, elem_classes='min_check')
 
        with gr.Column(scale=0.5, visible=False) as right_col:
            with gr.Tab(label='Setting'):
                size_image = gr.Dropdown(label="Escolha um tamanho para a imagem", choices=list(aspect_ratios.keys()))
                estilo_image = gr.Dropdown(label="Escolha os estlilos", choices=[fooocus_expansion] + style_keys,multiselect=True)
                negative_prompt = gr.Textbox(label='Negative Prompt', show_label=True, placeholder="Type prompt here.",
                                             info='Describing objects that you do not want to see.')
                seed_random = gr.Checkbox(label='Random', value=True)
                image_seed = gr.Number(label='Seed', value=0, precision=0, visible=False)

                def random_checked(r):
                    return gr.update(visible=not r)

                def refresh_seed(r, s):
                    if r:
                        return random.randint(1, 1024*1024*1024)
                    else:
                        return s

                seed_random.change(random_checked, inputs=[seed_random], outputs=[image_seed], queue=False)
         


        advanced_checkbox.change(lambda x: gr.update(visible=x), advanced_checkbox, right_col, queue=False)
        control=[estilo_image]
        run_button.click(fn=click,inputs=[control],outputs=[negative_prompt])

shared.gradio_root.launch(inbrowser=True)
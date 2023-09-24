import gradio as gr
import shared
import modules.html
import modules.flags as flags
from modules.sdxl_styles import style_keys,aspect_ratios,fooocus_expansion, default_styles


shared.gradio_root = gr.Blocks(title='Fooocus', css=modules.html.css).queue()
with shared.gradio_root:
    with gr.Row():
        with gr.Column():
            with gr.Tab(label='Setting'):
                size_image = gr.Dropdown(label="Escolha um tamanho para a imagem", choices=list(aspect_ratios.keys()))
                estilo_image = gr.CheckboxGroup(label="Escolha os estlilos", choices=[fooocus_expansion] + style_keys)

shared.gradio_root.launch()
# interface_gui.py
import gi
import matplotlib
matplotlib.use('GTK3Agg')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.figure import Figure
from simulador import simular

# ---------- Estilo (CSS) ----------
def carregar_css():
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path("style.css")
    Gdk.Screen.get_default().get_default()
    screen = Gdk.Screen.get_default()
    Gtk.StyleContext.add_provider_for_screen(
        screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

# ---------- Gráfico (estilo dark) ----------
matplotlib.rcParams.update({
    'figure.facecolor': '#1a1d23',
    'axes.facecolor': '#22262e',
    'axes.edgecolor': '#2d323c',
    'axes.labelcolor': '#8b92a3',
    'xtick.color': '#8b92a3',
    'ytick.color': '#8b92a3',
    'text.color': '#e6e9ef',
    'grid.color': '#2d323c',
    'font.family': 'monospace',
})

figura = Figure(figsize=(6, 2.2))
ax = figura.add_subplot(1, 1, 1)

def plotar_sinal(sinal, titulo):
    ax.clear()
    ax.step(range(len(sinal)), sinal, where='post', color='#5b8cff', linewidth=1.5)
    ax.set_title(titulo, color='#e6e9ef', fontsize=11, fontfamily='monospace')
    ax.grid(True, alpha=0.3)
    figura.tight_layout()
    figura.canvas.draw()

# ---------- Lógica ----------
def mostrar_etapas_tx(etapas):
    texto_tx = (
        f"texto:    {etapas['texto_original']}\n"
        f"bits:     {etapas['bits']}\n"
        f"+ edc:    {etapas['bits_com_edc']}\n"
        f"quadro:   {etapas['quadro']}"
    )
    GLib.idle_add(label_tx_corpo.set_text, texto_tx)
    GLib.idle_add(plotar_sinal, etapas['sinal'], "sinal — canal de transmissão")

def mostrar_etapas_rx(etapas):
    status = "✓ ok" if etapas['edc_ok'] else "✗ erro detectado"
    texto_rx = (
        f"quadro:   {etapas['quadro_demodulado']}\n"
        f"+ edc:    {etapas['bits_com_edc']}\n"
        f"edc:      {status}\n"
        f"bits:     {etapas['bits_finais']}\n"
        f"texto:    {etapas['texto_final']}"
    )
    GLib.idle_add(label_rx_corpo.set_text, texto_rx)

def on_enviar(button):
    texto = entry.get_text()
    if not texto:
        return
    mod = combo_mod.get_active_text()
    enq = combo_enq.get_active_text()
    edc = combo_edc.get_active_text()
    simular(texto, mod, enq, edc, mostrar_etapas_rx, mostrar_etapas_tx)

# ---------- Construção da janela ----------
window = Gtk.Window(title="SimulaRede")
window.set_default_size(820, 640)
window.connect("destroy", Gtk.main_quit)

root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
root.set_margin_top(20)
root.set_margin_bottom(20)
root.set_margin_start(20)
root.set_margin_end(20)
window.add(root)

# Cabeçalho
titulo = Gtk.Label(label="SimulaRede")
titulo.get_style_context().add_class("titulo")
titulo.set_halign(Gtk.Align.START)
root.pack_start(titulo, False, False, 0)

subtitulo = Gtk.Label(label="simulador de camada física e de enlace")
subtitulo.get_style_context().add_class("eyebrow")
subtitulo.set_halign(Gtk.Align.START)
root.pack_start(subtitulo, False, False, 0)

# Linha de entrada + controles
linha_controles = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
root.pack_start(linha_controles, False, False, 0)

entry = Gtk.Entry()
entry.set_placeholder_text("digite a mensagem...")
entry.set_hexpand(True)
linha_controles.pack_start(entry, True, True, 0)

combo_mod = Gtk.ComboBoxText()
for nome in ['nrz', 'manchester', 'bipolar', 'ask', 'fsk', 'qpsk', 'qam16']:
    combo_mod.append_text(nome)
combo_mod.set_active(0)
linha_controles.pack_start(combo_mod, False, False, 0)

combo_enq = Gtk.ComboBoxText()
for nome in ['contagem', 'flag_bytes', 'flag_bits']:
    combo_enq.append_text(nome)
combo_enq.set_active(0)
linha_controles.pack_start(combo_enq, False, False, 0)

combo_edc = Gtk.ComboBoxText()
for nome in ['paridade', 'checksum', 'crc', 'hamming']:
    combo_edc.append_text(nome)
combo_edc.set_active(0)
linha_controles.pack_start(combo_edc, False, False, 0)

button = Gtk.Button(label="Enviar")
button.get_style_context().add_class("enviar")
button.connect("clicked", on_enviar)
linha_controles.pack_start(button, False, False, 0)

# Painéis TX | RX lado a lado
linha_paineis = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=16)
root.pack_start(linha_paineis, False, False, 0)

# Painel TX
painel_tx = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
painel_tx.get_style_context().add_class("painel")
painel_tx.set_hexpand(True)

label_tx_titulo = Gtk.Label(label="TRANSMISSOR")
label_tx_titulo.get_style_context().add_class("eyebrow")
label_tx_titulo.set_halign(Gtk.Align.START)
painel_tx.pack_start(label_tx_titulo, False, False, 0)

label_tx_corpo = Gtk.Label(label="aguardando envio...")
label_tx_corpo.set_halign(Gtk.Align.START)
label_tx_corpo.set_line_wrap(True)
label_tx_corpo.set_xalign(0)
painel_tx.pack_start(label_tx_corpo, False, False, 0)

linha_paineis.pack_start(painel_tx, True, True, 0)

# Painel RX
painel_rx = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
painel_rx.get_style_context().add_class("painel")
painel_rx.set_hexpand(True)

label_rx_titulo = Gtk.Label(label="RECEPTOR")
label_rx_titulo.get_style_context().add_class("eyebrow")
label_rx_titulo.set_halign(Gtk.Align.START)
painel_rx.pack_start(label_rx_titulo, False, False, 0)

label_rx_corpo = Gtk.Label(label="aguardando recepção...")
label_rx_corpo.set_halign(Gtk.Align.START)
label_rx_corpo.set_line_wrap(True)
label_rx_corpo.set_xalign(0)
painel_rx.pack_start(label_rx_corpo, False, False, 0)

linha_paineis.pack_start(painel_rx, True, True, 0)

# Gráfico
canvas = FigureCanvas(figura)
root.pack_start(canvas, True, True, 0)

carregar_css()
window.show_all()
Gtk.main()
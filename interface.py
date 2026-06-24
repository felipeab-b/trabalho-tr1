import gi
import matplotlib
matplotlib.use('GTK3Agg')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.figure import Figure
from simulador import simular

figura = Figure(figsize=(5, 2))
ax = figura.add_subplot(1, 1, 1)

def plotar_sinal(sinal, titulo):
    ax.clear()
    ax.step(range(len(sinal)), sinal, where='post')
    ax.set_title(titulo)
    figura.canvas.draw()

def mostrar_etapas_tx(etapas):
    texto_tx = (
        f"TX → Texto: {etapas['texto_original']}\n"
        f"Bits: {etapas['bits']}\n"
        f"Com EDC: {etapas['bits_com_edc']}\n"
        f"Quadro: {etapas['quadro']}"
    )
    GLib.idle_add(label_tx.set_text, texto_tx)
    GLib.idle_add(plotar_sinal, etapas['sinal'], "Sinal TX")

def mostrar_etapas_rx(etapas):
    texto_rx = (
        f"RX → Quadro demodulado: {etapas['quadro_demodulado']}\n"
        f"Com EDC: {etapas['bits_com_edc']}\n"
        f"EDC OK: {etapas['edc_ok']}\n"
        f"Bits finais: {etapas['bits_finais']}\n"
        f"Texto recuperado: {etapas['texto_final']}"
    )
    GLib.idle_add(label_rx.set_text, texto_rx)

def on_enviar(button):
    texto = entry.get_text()
    mod = combo_mod.get_active_text()
    enq = combo_enq.get_active_text()
    edc = combo_edc.get_active_text()
    simular(texto, mod, enq, edc, mostrar_etapas_rx, mostrar_etapas_tx)

window = Gtk.Window(title="SimulaRede")
window.set_default_size(700, 600)
window.connect("destroy", Gtk.main_quit)

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
window.add(box)

entry = Gtk.Entry()
entry.set_placeholder_text("Digite o texto...")
box.pack_start(entry, False, False, 0)

combo_mod = Gtk.ComboBoxText()
for nome in ['nrz', 'manchester', 'bipolar', 'ask', 'fsk', 'qpsk', 'qam16']:
    combo_mod.append_text(nome)
combo_mod.set_active(0)
box.pack_start(combo_mod, False, False, 0)

combo_enq = Gtk.ComboBoxText()
for nome in ['contagem', 'flag_bytes', 'flag_bits']:
    combo_enq.append_text(nome)
combo_enq.set_active(0)
box.pack_start(combo_enq, False, False, 0)

combo_edc = Gtk.ComboBoxText()
for nome in ['paridade', 'checksum', 'crc']:
    combo_edc.append_text(nome)
combo_edc.set_active(0)
box.pack_start(combo_edc, False, False, 0)

button = Gtk.Button(label="Enviar")
button.connect("clicked", on_enviar)
box.pack_start(button, False, False, 0)

label_tx = Gtk.Label(label="TX aguardando...")
label_tx.set_line_wrap(True)
box.pack_start(label_tx, False, False, 0)

label_rx = Gtk.Label(label="RX aguardando...")
label_rx.set_line_wrap(True)
box.pack_start(label_rx, False, False, 0)

canvas = FigureCanvas(figura)
box.pack_start(canvas, True, True, 0)

window.show_all()
Gtk.main()
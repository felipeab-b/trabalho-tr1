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

def plotar_sinal(sinal):
    ax.clear()
    ax.step(range(len(sinal)), sinal, where='post')
    ax.set_title("Sinal TX")
    figura.canvas.draw()

def atualizar_tela(texto_recuperado, sinal, edc_ok):
    GLib.idle_add(label_resultado.set_text, f"Recebido: {texto_recuperado} | EDC OK: {edc_ok}")
    GLib.idle_add(plotar_sinal, sinal)

def on_enviar(button):
    texto = entry.get_text()
    mod = combo_mod.get_active_text()
    enq = combo_enq.get_active_text()
    edc = combo_edc.get_active_text()
    simular(texto, mod, enq, edc, atualizar_tela)

window = Gtk.Window(title="SimulaRede")
window.set_default_size(600, 500)
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

label_resultado = Gtk.Label(label="Aguardando...")
box.pack_start(label_resultado, False, False, 0)

canvas = FigureCanvas(figura)
box.pack_start(canvas, True, True, 0)

window.show_all()
Gtk.main()
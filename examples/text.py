import pytest
from .config import PORT_DEFAULT
import time
from pynextion import PySerialNex
from pynextion.widgets import NexPage, NexText
from pynextion.constants import Alignment
from pynextion.color import NamedColor
from pynextion.resources import Font


@pytest.mark.parametrize("port", [PORT_DEFAULT])
def test_text(port):
    nexSerial = PySerialNex(port)

    print("Init")
    nexSerial.init()

    print("Create objects")
    nexPage = NexPage(nexSerial, "pg_text", pid=2)

    # nexText = NexText(nexSerial, "t1", pid=2, cid=1)
    # nexText = NexText(nexSerial, "t1")
    nexText = NexText(nexSerial, "t1", cid=1)

    print("Reset")
    nexSerial.reset()

    time.sleep(1)

    nexPage.show()

    time.sleep(1)

    msg = "Hello"
    nexText.text = msg

    time.sleep(1)
    assert nexText.text == msg

    time.sleep(0.5)

    nexText.backcolor = NamedColor.BLUE
    nexText.text = "1"

    time.sleep(0.5)

    nexText.backcolor = NamedColor.WHITE
    nexText.text = "2"

    time.sleep(0.5)

    nexText.backcolor = NamedColor.RED
    nexText.text = "3"

    time.sleep(0.5)

    nexText.text = "Bye nexText"

    time.sleep(0.5)

    nexText.visible = False
    nexText.backcolor = NamedColor.WHITE

    time.sleep(2)

    nexText.visible = True

    time.sleep(0.5)

    nexText.alignment.horizontal = Alignment.Horizontal.RIGHT
    nexText.alignment.vertical = Alignment.Vertical.DOWN
    nexText.forecolor = NamedColor.BLUE

    # Change fontid from 0 to 1
    nexText.font = Font(1)

    # nexSerial.reset()
    # time.sleep(0.5)

    nexSerial.close()

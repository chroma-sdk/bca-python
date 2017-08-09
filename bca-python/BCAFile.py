from enum import Enum


class ChromaAnimation:
    def __init__(self):
        self.FPS = 0
        self.Frames = []


class BCA:

    class FileHeader:
        def __init__(self):
            self.HEADERSIZE = 14
            self.ftype = 0
            self.fsize = 0
            self.fReserved = 0
            self.fBcaOffset = 0

    class BcaHeader:
        def __init__(self):
            self.hSize = 0
            self.hVersion = 0
            self.hFrameOffset = 0
            self.hFPS = 0
            self.hFrameCount = 0
            self.hReserved = 0

    class FrameHeader:
        def __init__(self):
            self.fhSize = 0
            self.fhDeviceCount = 0
            self.fhDataSize = 0

    class DeviceHeader:
        def __init__(self):
            self.dhSize = 0
            self.dhDatatype = 0
            self.dhDevice = 0
            self.dhDataSize = 0

    class DeviceData:
        def __init__(self):
            self.dRow = 0
            self.dCol = 0
            self.dABGR = 0

    class DeviceType(Enum):
        none = 0x0
        Keyboard = 0x1
        Keypad = 0x2
        Mouse = 0x3
        Mousepad = 0x4
        Headset = 0x5

    class DataType(Enum):
        AssignAll = 0
        AssignNamed = 1

    FrameList = None
    BHeader = None
    FHeader = None

    def __init__(self):
        self.BHeader = self.BcaHeader()
        self.FHeader = self.FileHeader()
        self.FrameList = []



class BinaryDevice:
    def __init__(self):
        self.DeviceHeader = BCA.DeviceHeader()
        self.DeviceDataList = []


class BinaryFrame:
    def __init__(self):
        self.FrameHeader = BCA.FrameHeader()
        self.DeviceList = []

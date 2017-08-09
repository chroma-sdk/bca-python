from .BCAFile import BCA, BinaryDevice, BinaryFrame
import struct


class BCAReader:
    def read(self, filename):
        try:
            with open(filename, "rb") as f:
                binary_file = BCA()

                """Reading FileHeader"""
                binary_file.FHeader.ftype = struct.unpack("<H", f.read(2))[0]
                binary_file.FHeader.fsize = struct.unpack("<L", f.read(4))[0]
                binary_file.FHeader.fReserved = struct.unpack("<L", f.read(4))[0]
                binary_file.FHeader.fBcaOffset = struct.unpack("<L", f.read(4))[0]
                """Reading BCAHeader"""
                binary_file.BHeader.hSize = struct.unpack("<L", f.read(4))[0]
                binary_file.BHeader.hVersion = struct.unpack("<H", f.read(2))[0]
                binary_file.BHeader.hFrameOffset = struct.unpack("<L", f.read(4))[0]
                binary_file.BHeader.hFPS = struct.unpack("<H", f.read(2))[0]
                binary_file.BHeader.hFrameCount = struct.unpack("<L", f.read(4))[0]
                binary_file.BHeader.hReserved = struct.unpack("<H", f.read(2))[0]

                """Reading Frame"""

                for h in range(0, int(binary_file.BHeader.hFrameCount)):
                    binary_file.FrameList.append(BinaryFrame())
                for i in range(0, int(binary_file.BHeader.hFrameCount)):
                    """Reading FrameHeader"""
                    binary_file.FrameList[i].FrameHeader.fhSize = struct.unpack("<H", f.read(2))[0]

                    binary_file.FrameList[i].FrameHeader.fhDeviceCount = struct.unpack("<H", f.read(2))[0]
                    for j in range(0, binary_file.FrameList[i].FrameHeader.fhDeviceCount):
                        binary_file.FrameList[i].DeviceList.append(BinaryDevice())

                    binary_file.FrameList[i].FrameHeader.fhDataSize = struct.unpack("<H", f.read(2))[0]
                    """Reading Frame Data"""

                    for j in range(0, len(binary_file.FrameList[i].DeviceList)):
                        binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhSize = struct.unpack("<B",
                                                                                                   f.read(1))[0]

                        binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhDatatype = struct.unpack("<B",
                                                                                                       f.read(1))[0]

                        binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhDevice = struct.unpack("<H",
                                                                                                     f.read(2))[0]

                        binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhDataSize = struct.unpack("<H",
                                                                                                       f.read(2))[0]

                        dataCount = int(binary_file.FrameList[i].DeviceList[j].DeviceHeader.dhDataSize / 6)
                        for k in range(0, dataCount):
                            binary_file.FrameList[i].DeviceList[j].DeviceDataList.append(BCA.DeviceData())
                        """Reading Device Data"""
                        for k in range(0, len(binary_file.FrameList[i].DeviceList[j].DeviceDataList)):
                            binary_file.FrameList[i].DeviceList[j].DeviceDataList[k].dRow = struct.unpack("<B",
                                                                                                          f.read(1))[0]
                            binary_file.FrameList[i].DeviceList[j].DeviceDataList[k].dCol = struct.unpack("<B",
                                                                                                          f.read(1))[0]
                            binary_file.FrameList[i].DeviceList[j].DeviceDataList[k].dABGR = struct.unpack("<L",
                                                                                                           f.read(4))[0]
                return binary_file
        except:
            # TODO Add proper exception handling
            print('Unexpected Error!')
            raise

# automatically generated by the FlatBuffers compiler, do not modify

# namespace: graphpipe

import flatbuffers

class MetadataRequest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMetadataRequest(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MetadataRequest()
        x.Init(buf, n + offset)
        return x

    # MetadataRequest
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def MetadataRequestStart(builder): builder.StartObject(0)
def MetadataRequestEnd(builder): return builder.EndObject()
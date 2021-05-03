from py_mplus import MPData
from py_mplus.objects import MPObject


class Mopub(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.unit_id = buffer.string()
        else:
            buffer.skip_type(skip)

'''
  switch (i >>> 3) {
    case 1:
      r.unitID = e.string();
      break;
    default:
      e.skipType(7 & i);
      break
'''
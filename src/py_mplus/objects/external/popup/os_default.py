from py_mplus.objects import MPObject, MPData
from py_mplus.objects.external.popup.button import Button


class OSDefault(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.subject = buffer.string()
        elif category == 2:
            self.body = buffer.string()
        elif category == 3:
            self.ok_button = Button(buffer, buffer.uint32())
        elif category == 4:
            self.neutral_button = Button(buffer, buffer.uint32())
        elif category == 5:
            self.cancel_button = Button(buffer, buffer.uint32())
        else:
            buffer.skip_type(skip)

'''
    e.decode = function (e, t) {
      e instanceof x || (e = x.create(e));
      var n = void 0 === t ? e.len : e.pos + t,
      r = new R.Proto.Popup.OSDefault;
      while (e.pos < n) {
        var a = e.uint32();
        switch (a >>> 3) {
          case 1:
            r.subject = e.string();
            break;
          case 2:
            r.body = e.string();
            break;
          case 3:
            r.okButton = R.Proto.Popup.Button.decode(e, e.uint32());
            break;
          case 4:
            r.neutralButton = R.Proto.Popup.Button.decode(e, e.uint32());
            break;
          case 5:
            r.cancelButton = R.Proto.Popup.Button.decode(e, e.uint32());
            break;
          default:
            e.skipType(7 & a);
            break
        }
      }
      return r
    }
'''
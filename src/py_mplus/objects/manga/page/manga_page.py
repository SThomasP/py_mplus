from py_mplus.objects import MPData, MPObject

TYPES = ['SINGLE', 'LEFT', 'RIGHT', 'DOUBLE']


class MangaPage(MPObject):
    def _decode(self, buffer: MPData, a, i):
        if a == 1:
            self.image = buffer.string()
        elif a == 2:
            self.width = buffer.uint32()
        elif a == 3:
            self.height = buffer.uint32()
        elif a == 4:
            self.type = buffer.int32()
        elif a == 5:
            self.encryption_key = buffer.string()
        else:
            buffer.skip_type(7 & i)


'''
    e.decode = function (e, t) {
      e instanceof x || (e = x.create(e));
      var n = void 0 === t ? e.len : e.pos + t,
      r = new R.Proto.Page.MangaPage;
      while (e.pos < n) {
        var a = e.uint32();
        switch (a >>> 3) {
          case 1:
            r.imageUrl = e.string();
            break;
          case 2:
            r.width = e.uint32();
            break;
          case 3:
            r.height = e.uint32();
            break;
          case 4:
            r.type = e.int32();
            break;
          case 5:
            r.encryptionKey = e.string();
            break;
          default:
            e.skipType(7 & a);
            break
        }
      }
      return r
    }
'''
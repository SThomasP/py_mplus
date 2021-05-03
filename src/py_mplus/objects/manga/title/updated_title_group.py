from py_mplus.objects import MPObject, MPData
from py_mplus.objects.manga.title.updated_title import UpdatedTitle


class UpdatedTitleGroup(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.group_name = buffer.string()
        elif category == 2:
            if not hasattr(self, 'titles'):
                self.titles = []
            self.titles.append(UpdatedTitle(buffer, buffer.uint32()))
        else:
            buffer.skip_type(skip)

'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.UpdatedTitleGroup;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.groupName = e.string();
          break;
        case 2:
          r.titles && r.titles.length || (r.titles = [
          ]),
          r.titles.push(R.Proto.UpdatedTitle.decode(e, e.uint32()));
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''
from py_mplus.objects import MPObject

LANGUAGES = ['ENGLISH', 'SPANISH']


class Title(MPObject):
    def _decode(self, buffer, category, skip):
        if category == 1:
            self.title_id = buffer.uint32()
        elif category == 2:
            self.name = buffer.string()
        elif category == 3:
            self.author = buffer.string()
        elif category == 4:
            self.portrait_image = buffer.string()  # subtitle
        elif category == 5:
            self.landscape_image = buffer.string()  # thumbnail
        elif category == 6:
            self.view_count = buffer.uint32()
        elif category == 7:
            self.language = buffer.int32()  # end date
        else:
            buffer.skip_type(skip)

'''
e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.Title;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.titleId = e.uint32();
          break;
        case 2:
          r.name = e.string();
          break;
        case 3:
          r.author = e.string();
          break;
        case 4:
          r.portraitImageUrl = e.string();
          break;
        case 5:
          r.landscapeImageUrl = e.string();
          break;
        case 6:
          r.viewCount = e.uint32();
          break;
        case 7:
          r.language = e.int32();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
'''
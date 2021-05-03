from py_mplus.objects import MPObject, MPData


class Comment(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.id = buffer.uint32()
        elif category == 2:
            self.index = buffer.uint32()
        elif category == 3:
            self.username = buffer.string()
        elif category == 4:
            self.icon_url = buffer.string()
        elif category == 6:
            self.is_my_comment = buffer.boolean()
        elif category == 7:
            self.already_liked = buffer.boolean()
        elif category == 9:
            self.number_of_likes = buffer.uint32()
        elif category == 10:
            self.body = buffer.string()
        elif category == 11:
            self.created = buffer.uint32()
        else:
            buffer.skip_type(skip)



'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.Comment;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.id = e.uint32();
          break;
        case 2:
          r.index = e.uint32();
          break;
        case 3:
          r.userName = e.string();
          break;
        case 4:
          r.iconUrl = e.string();
          break;
        case 6:
          r.isMyComment = e.bool();
          break;
        case 7:
          r.alreadyLiked = e.bool();
          break;
        case 9:
          r.numberOfLikes = e.uint32();
          break;
        case 10:
          r.body = e.string();
          break;
        case 11:
          r.created = e.uint32();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''
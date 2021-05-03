from py_mplus import MPData
from py_mplus.objects import MPObject
from py_mplus.objects.external.transition_action import TransitionAction


class PublisherNews(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.id = buffer.uint32()
        elif category == 2:
            self.publisher_id = buffer.uint32()
        elif category == 3:
            self.publisher_name = buffer.string()
        elif category == 4:
            self.subject = buffer.string()
        elif category == 5:
            self.body = buffer.string()
        elif category == 6:
            self.published_time_stamp = buffer.uint32()
        elif category == 7:
            self.action = TransitionAction(buffer, buffer.uint32())
        else:
            buffer.skip_type(skip)
'''
    e.decode = function (e, t) {
      e instanceof p || (e = p.create(e));
      var n = void 0 === t ? e.len : e.pos + t,
      a = new g.Proto.PublisherNews;
      while (e.pos < n) {
        var i = e.uint32();
        switch (i >>> 3) {
          case 1:
            a.id = e.uint32();
            break;
          case 2:
            a.publisherId = e.uint32();
            break;
          case 3:
            a.publisherName = e.string();
            break;
          case 4:
            a.subject = e.string();
            break;
          case 5:
            a.body = e.string();
            break;
          case 6:
            a.publishedTimeStamp = e.uint32();
            break;
          case 7:
            a.action = g.Proto.TransitionAction.decode(e, e.uint32());
            break;
          default:
            e.skipType(7 & i);
            break
        }
      }
      return a
'''
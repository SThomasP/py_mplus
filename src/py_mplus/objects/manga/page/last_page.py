from py_mplus.objects import MPObject, MPData
from py_mplus.objects.external.ad_network import AdNetwork
from py_mplus.objects.external.banner import Banner
from py_mplus.objects.external.popup import Popup
from py_mplus.objects.manga.chapter import Chapter
from py_mplus.objects.comment import Comment

CHAPTER_TYPES = ['LATEST', 'SEQUENCE', 'NO SEQUENCE']


class LastPage(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            self.current_chapter = Chapter(buffer, buffer.uint32())
        elif a == 2:
            self.next_chapter = Chapter(buffer, buffer.uint32())
        elif a == 3:
            if not hasattr(self, 'top_comments'):
                self.top_comments = []
            self.top_comments.append(Comment(buffer, buffer.uint32()))
        elif a == 4:
            self.subscribed = buffer.boolean()
        elif a == 5:
            self.next_time_stamp = buffer.uint32()
        elif a == 6:
            self.chapter_type = buffer.int32()
        elif a == 7:
            self.advertisement = AdNetwork(buffer, buffer.uint32())
        elif a == 8:
            self.movieReward = Popup(buffer, buffer.uint32())
        elif a == 9:
            if not hasattr(self, 'banners'):
                self.banners = []
            self.banners.append(Banner(buffer, buffer.uint32()))
        else:
            buffer.skip_type(7 & a)

'''
      switch (i >>> 3) {
        case 1:
          r.currentChapter = m.Proto.Chapter.decode(e, e.uint32());
          break;
        case 2:
          r.nextChapter = m.Proto.Chapter.decode(e, e.uint32());
          break;
        case 3:
          r.topComments && r.topComments.length || (r.topComments = [
          ]),
          r.topComments.push(m.Proto.Comment.decode(e, e.uint32()));
          break;
        case 4:
          r.isSubscribed = e.bool();
          break;
        case 5:
          r.nextTimeStamp = e.uint32();
          break;
        case 6:
          r.chapterType = e.int32();
          break;
        case 7:
          r.advertisement = m.Proto.AdNetworkList.decode(e, e.uint32());
          break;
        case 8:
          r.movieReward = m.Proto.Popup.decode(e, e.uint32());
          break;
        case 9:
          r.banners && r.banners.length || (r.banners = [
          ]),
          r.banners.push(m.Proto.Banner.decode(e, e.uint32()));
          break;
        default:
          e.skipType(7 & i);
          break
'''
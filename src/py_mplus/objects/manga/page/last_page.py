from py_mplus.objects import MPObject, MPData
from py_mplus.objects.external.ad_network import AdNetwork
from py_mplus.objects.external.banner import Banner
from py_mplus.objects.external.popup import Popup
from py_mplus.objects.manga.chapter import Chapter
from py_mplus.objects.comment import Comment
from py_mplus.objects.manga.title import Title
from py_mplus.objects.user.user_tickets import UserTickets

CHAPTER_TYPES = ['LATEST', 'SEQUENCE', 'NO SEQUENCE']


class LastPage(MPObject):
    def _decode(self, buffer: MPData, a, i):
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
        elif a == 10:
            if not hasattr(self, 'ticket_titles'):
                self.ticket_titles = []
            self.ticket_titles.append(Title(buffer, buffer.uint32()))
        elif a == 11:
            self.publisher_banner = Banner(buffer, buffer.uint32())
        elif a == 12:
            self.user_ticket = UserTickets(buffer, buffer.uint32())
        elif a == 13:
            self.is_next_chapter_read_by_ticket = buffer.boolean()
        else:
            buffer.skip_type(7 & i)

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
        case 10:
          a.ticketTitleList && a.ticketTitleList.length || (a.ticketTitleList = [
          ]),
          a.ticketTitleList.push(g.Proto.Title.decode(e, e.uint32()));
          break;
        case 11:
          a.publisherBanner = g.Proto.Banner.decode(e, e.uint32());
          break;
        case 12:
          a.userTickets = g.Proto.UserTickets.decode(e, e.uint32());
          break;
        case 13:
          a.isNextChapterReadByTicket = e.bool();
          break;
        default:
          e.skipType(7 & i);
          break
'''
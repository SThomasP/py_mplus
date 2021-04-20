from py_mplus.objects import MPObject
from py_mplus.objects.manga.title import Title
from py_mplus.objects.manga.chapter import Chapter
from py_mplus.objects.external.banner import Banner
from py_mplus.objects.external.sns import SNS
from py_mplus.objects.user.user_tickets import UserTickets
from py_mplus.objects.views.title_detail_view.publisher_item import PublisherItem

UPDATE_TIMINGS = ['NOT_REGULARLY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'DAY']
RATINGS = ['ALL_AGES', 'TEEN', 'TEEN_PLUS', 'MATURE']


class TitleDetailView(MPObject):
    def _decode(self, buffer, a, i):
        if a == 1:
            self.title = Title(buffer, buffer.uint32())
        elif a == 2:
            self.image = buffer.string()
        elif a == 3:
            self.overview = buffer.string()
        elif a == 4:
            self.background_image = buffer.string()
        elif a == 5:
            self.next_time_stamp = buffer.uint32()
        elif a == 6:
            self.update_timing = buffer.int32()
        elif a == 7:
            self.viewing_period_description = buffer.string()
        elif a == 8:
            self.non_appearance_info = buffer.string()
        elif a == 9:
            if not hasattr(self, 'first_chapters'):
                self.first_chapters = []
            self.first_chapters.append(Chapter(buffer, buffer.uint32()))
        elif a == 10:
            if not hasattr(self, 'last_chapters'):
                self.last_chapters = []
            self.last_chapters.append(Chapter(buffer, buffer.uint32()))
        elif a == 11:
            if not hasattr(self, 'banners'):
                self.banners = []
            self.banners.append(Banner(buffer, buffer.uint32()))
        elif a == 12:
            if not hasattr(self, 'recommended_titles'):
                self.recommended_titles = []
            self.recommended_titles.append(Title(buffer, buffer.uint32()))
        elif a == 13:
            self.sns_info = SNS(buffer, buffer.uint32())
        elif a == 14:
            self.is_simul_release = buffer.boolean()
        elif a == 15:
            self.is_subscribed = buffer.boolean()
        elif a == 16:
            self.rating = buffer.int32()
        elif a == 17:
            self.chapters_descending = buffer.boolean()
        elif a == 18:
            self.number_of_views = buffer.uint32()
        elif a == 19:
            if not hasattr(self, 'publisher_items'):
                self.publisher_items = []
            self.publisher_items.append(PublisherItem(buffer, buffer.uint32()))
        elif a == 20:
            if not hasattr(self, 'title_banners'):
                self.title_banners = []
            self.title_banners.append(Banner(buffer, buffer.uint32()))
        elif a == 21:
            self.user_tickets = UserTickets(buffer, buffer.uint32())
        elif a == 22:
            if not hasattr(self, 'ticket_chapters'):
                self.ticket_chapters = []
            self.ticket_chapters.append(Chapter(buffer, buffer.uint32()))
        elif a == 23:
            if not hasattr(self, 'ticket_titles'):
                self.ticket_titles = []
            self.ticket_titles.append(Title(buffer, buffer.uint32()))
        elif a == 24:
            self.has_chapters_between = buffer.boolean()
        elif a == 25:
            self.publisher_banner = Banner(buffer, buffer.uint32())
        else:
            buffer.skip_type(7 & i)



'''
e.decode = function (e, t) {
  e instanceof p || (e = p.create(e));
  var n = void 0 === t ? e.len : e.pos + t,
  a = new g.Proto.TitleDetailView;
  while (e.pos < n) {
    var i = e.uint32();
    switch (i >>> 3) {
      case 1:
        a.title = g.Proto.Title.decode(e, e.uint32());
        break;
      case 2:
        a.titleImageUrl = e.string();
        break;
      case 3:
        a.overview = e.string();
        break;
      case 4:
        a.backgroundImageUrl = e.string();
        break;
      case 5:
        a.nextTimeStamp = e.uint32();
        break;
      case 6:
        a.updateTiming = e.int32();
        break;
      case 7:
        a.viewingPeriodDescription = e.string();
        break;
      case 8:
        a.nonAppearanceInfo = e.string();
        break;
      case 9:
        a.firstChapterList && a.firstChapterList.length || (a.firstChapterList = [
        ]),
        a.firstChapterList.push(g.Proto.Chapter.decode(e, e.uint32()));
        break;
      case 10:
        a.lastChapterList && a.lastChapterList.length || (a.lastChapterList = [
        ]),
        a.lastChapterList.push(g.Proto.Chapter.decode(e, e.uint32()));
        break;
      case 11:
        a.banners && a.banners.length || (a.banners = [
        ]),
        a.banners.push(g.Proto.Banner.decode(e, e.uint32()));
        break;
      case 12:
        a.recommendedTitleList && a.recommendedTitleList.length || (a.recommendedTitleList = [
        ]),
        a.recommendedTitleList.push(g.Proto.Title.decode(e, e.uint32()));
        break;
      case 13:
        a.sns = g.Proto.Sns.decode(e, e.uint32());
        break;
      case 14:
        a.isSimulReleased = e.bool();
        break;
      case 15:
        a.isSubscribed = e.bool();
        break;
      case 16:
        a.rating = e.int32();
        break;
      case 17:
        a.chaptersDescending = e.bool();
        break;
      case 18:
        a.numberOfViews = e.uint32();
        break;
      case 19:
        a.publisherItems && a.publisherItems.length || (a.publisherItems = [
        ]),
        a.publisherItems.push(g.Proto.TitleDetailView.PublisherItem.decode(e, e.uint32()));
        break;
      case 20:
        a.titleBanners && a.titleBanners.length || (a.titleBanners = [
        ]),
        a.titleBanners.push(g.Proto.Banner.decode(e, e.uint32()));
        break;
      case 21:
        a.userTickets = g.Proto.UserTickets.decode(e, e.uint32());
        break;
      case 22:
        a.ticketChapterList && a.ticketChapterList.length || (a.ticketChapterList = [
        ]),
        a.ticketChapterList.push(g.Proto.Chapter.decode(e, e.uint32()));
        break;
      case 23:
        a.ticketTitleList && a.ticketTitleList.length || (a.ticketTitleList = [
        ]),
        a.ticketTitleList.push(g.Proto.Title.decode(e, e.uint32()));
        break;
      case 24:
        a.hasChaptersBetween = e.bool();
        break;
      case 25:
        a.publisherBanner = g.Proto.Banner.decode(e, e.uint32());
        break;
      default:
        e.skipType(7 & i);
        break
    }
  }
  return a
'''
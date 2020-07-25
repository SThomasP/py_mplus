from mplus.objects import MPObject
from mplus.objects.manga.title import Title
from mplus.objects.manga.chapter import Chapter
from mplus.objects.external.banner import Banner
from mplus.objects.external.sns import SNS

UPDATE_TIMINGS = ['NOT_REGULARLY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'DAY']
RATINGS = ['ALL_AGES', 'TEEN', 'TEEN_PLUS', 'MATURE']


class TitleDetailView(MPObject):
    def _decode(self, buffer, a):
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
        else:
            buffer.skip_type(7 & a)



'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.TitleDetailView;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.title = R.Proto.Title.decode(e, e.uint32());
          break;
        case 2:
          r.titleImageUrl = e.string();
          break;
        case 3:
          r.overview = e.string();
          break;
        case 4:
          r.backgroundImageUrl = e.string();
          break;
        case 5:
          r.nextTimeStamp = e.uint32();
          break;
        case 6:
          r.updateTiming = e.int32();
          break;
        case 7:
          r.viewingPeriodDescription = e.string();
          break;
        case 8:
          r.nonAppearanceInfo = e.string();
          break;
        case 9:
          r.firstChapterList && r.firstChapterList.length || (r.firstChapterList = [
          ]),
          r.firstChapterList.push(R.Proto.Chapter.decode(e, e.uint32()));
          break;
        case 10:
          r.lastChapterList && r.lastChapterList.length || (r.lastChapterList = [
          ]),
          r.lastChapterList.push(R.Proto.Chapter.decode(e, e.uint32()));
          break;
        case 11:
          r.banners && r.banners.length || (r.banners = [
          ]),
          r.banners.push(R.Proto.Banner.decode(e, e.uint32()));
          break;
        case 12:
          r.recommendedTitleList && r.recommendedTitleList.length || (r.recommendedTitleList = [
          ]),
          r.recommendedTitleList.push(R.Proto.Title.decode(e, e.uint32()));
          break;
        case 13:
          r.sns = R.Proto.Sns.decode(e, e.uint32());
          break;
        case 14:
          r.isSimulReleased = e.bool();
          break;
        case 15:
          r.isSubscribed = e.bool();
          break;
        case 16:
          r.rating = e.int32();
          break;
        case 17:
          r.chaptersDescending = e.bool();
          break;
        case 18:
          r.numberOfViews = e.uint32();
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
'''
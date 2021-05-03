from py_mplus.objects import MPObject, MPData
from py_mplus.objects.user.registration_data import RegistrationData

from py_mplus.objects.views.featured_titles_view import FeaturedTitlesView
from py_mplus.objects.views.all_titles_view import AllTitlesView
from py_mplus.objects.views.comment_list_view import CommentListView
from py_mplus.objects.views.feedback_view import FeedbackView
from py_mplus.objects.views.home_view import HomeView
from py_mplus.objects.views.initial_view import InitialView
from py_mplus.objects.views.manga_viewer import MangaViewer
from py_mplus.objects.views.profile_settings_view import ProfileSettingsView
from py_mplus.objects.views.service_announcements_view import ServiceAnnouncementsView
from py_mplus.objects.views.settings_view import SettingsView
from py_mplus.objects.views.subscribed_titles_view import SubscribedTitlesView
from py_mplus.objects.views.title_detail_view import TitleDetailView
from py_mplus.objects.views.title_ranking_view import TitleRankingView
from py_mplus.objects.views.update_profile_results_view import UpdateProfileResultsView
from py_mplus.objects.views.web_home_view import WebHomeView


class SuccessResult(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            self.is_featured_update = buffer.boolean()
        elif category == 2:
            self.registration_data = RegistrationData(buffer, buffer.uint32())
        elif category == 3:
            self.home_view = HomeView(buffer, buffer.uint32())
        elif category == 4:
            self.featured_titles_view = FeaturedTitlesView(buffer, buffer.uint32())
        elif category == 5:
            self.all_titles_view = AllTitlesView(buffer, buffer.uint32())
        elif category == 6:
            self.title_ranking_view = TitleRankingView(buffer, buffer.uint32())
        elif category == 7:
            self.subscribed_titles_view = SubscribedTitlesView(buffer, buffer.uint32())
        elif category == 8:
            self.title_detail_view = TitleDetailView(buffer, buffer.uint32())
        elif category == 9:
            self.comment_list_view = CommentListView(buffer, buffer.uint32())
        elif category == 10:
            self.manga_viewer = MangaViewer(buffer, buffer.uint32())
        elif category == 11:
            self.web_home_view = WebHomeView(buffer, buffer.uint32())
        elif category == 12:
            self.settings_view = SettingsView(buffer, buffer.uint32())
        elif category == 13:
            self.profile_settings_view = ProfileSettingsView(buffer, buffer.uint32())
        elif category == 14:
            self.update_profile_results_view = UpdateProfileResultsView(buffer, buffer.uint32())
        elif category == 15:
            self.service_announcements_view = ServiceAnnouncementsView(buffer, buffer.uint32())
        elif category == 16:
            self.initial_view = InitialView(buffer, buffer.uint32())
        elif category == 17:
            self.feedback_view = FeedbackView(buffer, buffer.uint32())
        else:
            buffer.skip_type(skip)


'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.SuccessResult;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.isFeaturedUpdated = e.bool();
          break;
        case 2:
          r.registerationData = R.Proto.RegistrationData.decode(e, e.uint32());
          break;
        case 3:
          r.homeView = R.Proto.HomeView.decode(e, e.uint32());
          break;
        case 4:
          r.featuredTitlesView = R.Proto.FeaturedTitlesView.decode(e, e.uint32());
          break;
        case 5:
          r.allTitlesView = R.Proto.AllTitlesView.decode(e, e.uint32());
          break;
        case 6:
          r.titleRankingView = R.Proto.TitleRankingView.decode(e, e.uint32());
          break;
        case 7:
          r.subscribedTitlesView = R.Proto.SubscribedTitlesView.decode(e, e.uint32());
          break;
        case 8:
          r.titleDetailView = R.Proto.TitleDetailView.decode(e, e.uint32());
          break;
        case 9:
          r.commentListView = R.Proto.CommentListView.decode(e, e.uint32());
          break;
        case 10:
          r.mangaViewer = R.Proto.MangaViewer.decode(e, e.uint32());
          break;
        case 11:
          r.webHomeView = R.Proto.WebHomeView.decode(e, e.uint32());
          break;
        case 12:
          r.settingsView = R.Proto.SettingsView.decode(e, e.uint32());
          break;
        case 13:
          r.profileSettingsView = R.Proto.ProfileSettingsView.decode(e, e.uint32());
          break;
        case 14:
          r.updateProfileResultView = R.Proto.UpdateProfileResultView.decode(e, e.uint32());
          break;
        case 15:
          r.serviceAnnouncementsView = R.Proto.ServiceAnnouncementsView.decode(e, e.uint32());
          break;
        case 16:
          r.initialView = R.Proto.InitialView.decode(e, e.uint32());
          break;
        case 17:
          r.feedbackView = R.Proto.FeedbackView.decode(e, e.uint32());
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''
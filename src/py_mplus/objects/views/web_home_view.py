from py_mplus.objects import MPObject, MPData
from py_mplus.objects.external.banner import Banner
from py_mplus.objects.manga.title import Title
from py_mplus.objects.manga.title.updated_title_group import UpdatedTitleGroup


class WebHomeView(MPObject):
    def _decode(self, buffer: MPData, a, i):
        if a == 1:
            if not hasattr(self, 'top_banners'):
                self.top_banners = []
            self.top_banners.append(Banner(buffer, buffer.uint32()))
        elif a == 2:
            if not hasattr(self, 'groups'):
                self.groups = []
            self.groups.append(UpdatedTitleGroup(buffer, buffer.uint32()))
        elif a == 3:
            if not hasattr(self, 'ranking'):
                self.ranking = []
            self.ranking.append(Title(buffer, buffer.uint32()))
        else:
            buffer.skip_type(7 & i)


'''
e.decode = function (e, t) {
e instanceof x || (e = x.create(e));
var n = void 0 === t ? e.len : e.pos + t,
r = new R.Proto.WebHomeView;
while (e.pos < n) {
var a = e.uint32();
switch (a >>> 3) {
case 1:
r.topBanners && r.topBanners.length || (r.topBanners = [
]),
r.topBanners.push(R.Proto.Banner.decode(e, e.uint32()));
break;
case 2:
r.groups && r.groups.length || (r.groups = [
]),
r.groups.push(R.Proto.UpdatedTitleGroup.decode(e, e.uint32()));
break;
case 3:
r.ranking && r.ranking.length || (r.ranking = [
]),
r.ranking.push(R.Proto.Title.decode(e, e.uint32()));
break;
default:
e.skipType(7 & a);
break
}
}
return r
}
'''
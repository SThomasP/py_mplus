from py_mplus.objects import MPObject, MPData
from py_mplus.objects.external.service_announcement import ServiceAnnouncement


class ServiceAnnouncementsView(MPObject):
    def _decode(self, buffer: MPData, category, skip):
        if category == 1:
            if not hasattr(self, 'service_announcements'):
                self.service_announcements = []
            self.service_announcements.append(ServiceAnnouncement(buffer, buffer.uint32()))
        else:
            buffer.skip_type(skip)


'''
e.decode = function (e, t) {
e instanceof x || (e = x.create(e));
var n = void 0 === t ? e.len : e.pos + t,
r = new R.Proto.ServiceAnnouncementsView;
while (e.pos < n) {
var a = e.uint32();
switch (a >>> 3) {
case 1:
r.serviceAnnouncements && r.serviceAnnouncements.length || (r.serviceAnnouncements = [
]),
r.serviceAnnouncements.push(R.Proto.ServiceAnnouncement.decode(e, e.uint32()));
break;
default:
e.skipType(7 & a);
break
}
}
return r
}
'''
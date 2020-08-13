from py_mplus.objects import MPObject, MPData
from py_mplus.objects.user.feedback import Feedback


class FeedbackView(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            if not hasattr(self, 'feedback_list'):
                self.feedback_list = []
            self.feedback_list.append(Feedback(buffer, buffer.uint32()))
        else:
            buffer.skip_type(7 & a)


'''
e.decode = function (e, t) {
e instanceof x || (e = x.create(e));
var n = void 0 === t ? e.len : e.pos + t,
r = new R.Proto.FeedbackView;
while (e.pos < n) {
var a = e.uint32();
switch (a >>> 3) {
case 1:
r.feedbackList && r.feedbackList.length || (r.feedbackList = [
]),
r.feedbackList.push(R.Proto.Feedback.decode(e, e.uint32()));
break;
default:
e.skipType(7 & a);
break
}
}
return r
}
'''
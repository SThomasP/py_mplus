from mplus.objects import MPObject, MPData
from mplus.objects.comment import Comment


class CommentListView(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            if not hasattr(self, 'comments'):
                self.comments = []
            self.comments.append(Comment(buffer, buffer.uint32()))
        elif a == 2:
            self.is_set_username = buffer.boolean()
        else:
            buffer.skip_type(7 & a)


'''
e.decode = function (e, t) {
e instanceof x || (e = x.create(e));
var n = void 0 === t ? e.len : e.pos + t,
r = new R.Proto.CommentListView;
while (e.pos < n) {
var a = e.uint32();
switch (a >>> 3) {
case 1:
r.comments && r.comments.length || (r.comments = [
]),
r.comments.push(R.Proto.Comment.decode(e, e.uint32()));
break;
case 2:
r.ifSetUserName = e.bool();
break;
default:
e.skipType(7 & a);
break
}
}
return r
}
'''
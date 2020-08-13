from py_mplus.objects import MPObject, MPData
from py_mplus.objects.manga.chapter import Chapter
from py_mplus.objects.manga.page import Page
from py_mplus.objects.external.sns import SNS


class MangaViewer(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            if not hasattr(self, 'pages'):
                self.pages = []
            self.pages.append(Page(buffer, buffer.uint32()))
        elif a == 2:
            self.chapter_id = buffer.uint32()
        elif a == 3:
            if not hasattr(self, 'chapters'):
                self.chapters = []
            self.chapters.append(Chapter(buffer, buffer.uint32()))
        elif a == 4:
            self.sns_info = SNS(buffer, buffer.uint32())
        elif a == 5:
            self.title_name = buffer.string()
        elif a == 6:
            self.chapter_name = buffer.string()
        elif a == 7:
            self.number_of_comments = buffer.uint32()
        elif a == 8:
            self.is_vertical_only = buffer.boolean()
        elif a == 9:
            self.title_id = buffer.uint32()
        elif a == 10:
            self.start_from_right = buffer.boolean()
        else:
            buffer.skip_type(7 & a)

'''
e.decode = function (e, t) {
e instanceof x || (e = x.create(e));
var n = void 0 === t ? e.len : e.pos + t,
r = new R.Proto.MangaViewer;
while (e.pos < n) {
var a = e.uint32();
switch (a >>> 3) {
case 1:
r.pages && r.pages.length || (r.pages = [
]),
r.pages.push(R.Proto.Page.decode(e, e.uint32()));
break;
case 2:
r.chapterId = e.uint32();
break;
case 3:
r.chapters && r.chapters.length || (r.chapters = [
]),
r.chapters.push(R.Proto.Chapter.decode(e, e.uint32()));
break;
case 4:
r.sns = R.Proto.Sns.decode(e, e.uint32());
break;
case 5:
r.titleName = e.string();
break;
case 6:
r.chapterName = e.string();
break;
case 7:
r.numberOfComments = e.uint32();
break;
case 8:
r.isVerticalOnly = e.bool();
break;
case 9:
r.titleId = e.uint32();
break;
case 10:
r.startFromRight = e.bool();
break;
default:
e.skipType(7 & a);
break
}
}
return r
}
'''
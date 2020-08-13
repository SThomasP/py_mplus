from py_mplus.objects import MPObject, MPData


class InitialView(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            self.gdpr_agreement_required = buffer.boolean()
        elif a == 2:
            self.english_titles_count = buffer.uint32()
        elif a == 3:
            self.spanish_titles_count = buffer.uint32()
        else:
            buffer.skip_type(7 & a)


'''
e.decode = function (e, t) {
e instanceof x || (e = x.create(e));
var n = void 0 === t ? e.len : e.pos + t,
r = new R.Proto.InitialView;
while (e.pos < n) {
var a = e.uint32();
switch (a >>> 3) {
case 1:
r.gdprAgreementRequired = e.bool();
break;
case 2:
r.englishTitlesCount = e.uint32();
break;
case 3:
r.spanishTitlesCount = e.uint32();
break;
default:
e.skipType(7 & a);
break
}
}
return r
}
'''
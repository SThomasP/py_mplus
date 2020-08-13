from py_mplus.objects import MPObject, MPData

from py_mplus.objects.external.ad_network.admob import Admob
from py_mplus.objects.external.ad_network.adsense import Adsense
from py_mplus.objects.external.ad_network.applovin import AppLoving
from py_mplus.objects.external.ad_network.facebook import Facebook
from py_mplus.objects.external.ad_network.mopub import Mopub


class AdNetwork(MPObject):
    def _decode(self, buffer: MPData, a):
        if a == 1:
            self.facebook = Facebook(buffer, buffer.uint32())
        elif a == 2:
            self.admob = Admob(buffer, buffer.uint32())
        elif a == 3:
            self.mopub = Mopub(buffer, buffer.uint32())
        elif a == 4:
            self.adsense = Adsense(buffer, buffer.uint32())
        elif a == 5:
            self.applovin = AppLoving(buffer, buffer.uint32())
        else:
            buffer.skip_type(7 & a)

'''
  r = new m.Proto.AdNetwork;
  while (e.pos < n) {
    var i = e.uint32();
    switch (i >>> 3) {
      case 1:
        r.facebook = m.Proto.AdNetwork.Facebook.decode(e, e.uint32());
        break;
      case 2:
        r.admob = m.Proto.AdNetwork.Admob.decode(e, e.uint32());
        break;
      case 3:
        r.mopub = m.Proto.AdNetwork.Mopub.decode(e, e.uint32());
        break;
      case 4:
        r.adsense = m.Proto.AdNetwork.Adsense.decode(e, e.uint32());
        break;
      case 5:
        r.applovin = m.Proto.AdNetwork.Applovin.decode(e, e.uint32());
        break;
      default:
        e.skipType(7 & i);
        break
    }
  }
'''
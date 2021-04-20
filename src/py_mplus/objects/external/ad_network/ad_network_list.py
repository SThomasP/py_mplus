from py_mplus.objects import MPObject, MPData
from py_mplus.objects.external.ad_network import AdNetwork


class AdNetworkList(MPObject):
    def _decode(self, buffer: MPData, a, i):
        if a == 1:
            if not hasattr(self, 'ad_networks'):
                self.ad_networks = []
            self.ad_networks.append(AdNetwork(buffer, buffer.uint32()))
        else:
            buffer.skip_type(7 & i)

'''
  e.decode = function (e, t) {
    e instanceof x || (e = x.create(e));
    var n = void 0 === t ? e.len : e.pos + t,
    r = new R.Proto.AdNetworkList;
    while (e.pos < n) {
      var a = e.uint32();
      switch (a >>> 3) {
        case 1:
          r.adNetworks && r.adNetworks.length || (r.adNetworks = [
          ]),
          r.adNetworks.push(R.Proto.AdNetwork.decode(e, e.uint32()));
          break;
        default:
          e.skipType(7 & a);
          break
      }
    }
    return r
  }
'''


u.prototype.uint32 = function () {
var t = 4294967295;
return function () {
  if (t = (127 & this.buf[this.pos]) >>> 0, this.buf[this.pos++] < 128) return t;
  if (t = (t | (127 & this.buf[this.pos]) << 7) >>> 0, this.buf[this.pos++] < 128) return t;
  if (t = (t | (127 & this.buf[this.pos]) << 14) >>> 0, this.buf[this.pos++] < 128) return t;
  if (t = (t | (127 & this.buf[this.pos]) << 21) >>> 0, this.buf[this.pos++] < 128) return t;
  if (t = (t | (15 & this.buf[this.pos]) << 28) >>> 0, this.buf[this.pos++] < 128) return t;
  if ((this.pos += 5) > this.len) throw this.pos = this.len,
  s(this, 10);
  return t
}
}(),
u.prototype.int32 = function () {
return 0 | this.uint32()
},
u.prototype.sint32 = function () {
var t = this.uint32();
return t >>> 1 ^ - (1 & t) | 0
},
u.prototype.bool = function () {
return 0 !== this.uint32()
},
u.prototype.fixed32 = function () {
if (this.pos + 4 > this.len) throw s(this, 4);
return d(this.buf, this.pos += 4)
},
u.prototype.sfixed32 = function () {
if (this.pos + 4 > this.len) throw s(this, 4);
return 0 | d(this.buf, this.pos += 4)
},
u.prototype.float = function () {
if (this.pos + 4 > this.len) throw s(this, 4);
var t = i.float.readFloatLE(this.buf, this.pos);
return this.pos += 4,
t
},
u.prototype.double = function () {
if (this.pos + 8 > this.len) throw s(this, 4);
var t = i.float.readDoubleLE(this.buf, this.pos);
return this.pos += 8,
t
},
u.prototype.bytes = function () {
var t = this.uint32(),
e = this.pos,
n = this.pos + t;
if (n > this.len) throw s(this, t);
return this.pos += t,
Array.isArray(this.buf) ? this.buf.slice(e, n)  : e === n ? new this.buf.constructor(0)  : this._slice.call(this.buf, e, n)
},
u.prototype.string = function () {
var t = this.bytes();
return a.read(t, 0, t.length)
}

u.prototype.skip = function (t) {
if ('number' === typeof t) {
  if (this.pos + t > this.len) throw s(this, t);
  this.pos += t
} else do {
  if (this.pos >= this.len) throw s(this)
} while (128 & this.buf[this.pos++]);
return this
}

u.prototype.skipType = function (t) {
  switch (t) {
    case 0:
      this.skip();
      break;
    case 1:
      this.skip(8);
      break;
    case 2:
      this.skip(this.uint32());
      break;
    case 3:
      while (4 !== (t = 7 & this.uint32())) this.skipType(t);
      break;
    case 5:
      this.skip(4);
      break;
    default:
      throw Error('invalid wire type ' + t + ' at offset ' + this.pos)
  }
}
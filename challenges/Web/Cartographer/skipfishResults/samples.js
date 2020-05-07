var mime_samples = [
  { 'mime': 'image/png', 'samples': [
    { 'url': 'http://docker.hackthebox.eu:30982/logo.png', 'dir': '_m0/0', 'linked': 2, 'len': 4390 } ]
  },
  { 'mime': 'text/css', 'samples': [
    { 'url': 'http://docker.hackthebox.eu:30982/style.css', 'dir': '_m1/0', 'linked': 2, 'len': 2475 } ]
  },
  { 'mime': 'text/html', 'samples': [
    { 'url': 'http://docker.hackthebox.eu:30982/', 'dir': '_m2/0', 'linked': 2, 'len': 673 } ]
  }
];

var issue_samples = [
  { 'severity': 1, 'type': 20205, 'samples': [
    { 'url': 'http://docker.hackthebox.eu:30982/', 'extra': 'Responses too slow for time sensitive tests', 'sid': '0', 'dir': '_i0/0' } ]
  },
  { 'severity': 0, 'type': 10803, 'samples': [
    { 'url': 'http://docker.hackthebox.eu:30982/style.css', 'extra': '', 'sid': '0', 'dir': '_i1/0' } ]
  },
  { 'severity': 0, 'type': 10602, 'samples': [
    { 'url': 'http://docker.hackthebox.eu:30982/', 'extra': '', 'sid': '0', 'dir': '_i2/0' } ]
  },
  { 'severity': 0, 'type': 10205, 'samples': [
    { 'url': 'http://docker.hackthebox.eu:30982/sfi9876', 'extra': '', 'sid': '0', 'dir': '_i3/0' } ]
  },
  { 'severity': 0, 'type': 10202, 'samples': [
    { 'url': 'http://docker.hackthebox.eu:30982/', 'extra': 'Apache/2.4.18 (Ubuntu)', 'sid': '0', 'dir': '_i4/0' } ]
  }
];


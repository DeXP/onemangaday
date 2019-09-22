
var Module = typeof Module !== 'undefined' ? Module : {};

if (!Module.expectedDataFileDownloads) {
  Module.expectedDataFileDownloads = 0;
  Module.finishedDataFileDownloads = 0;
}
Module.expectedDataFileDownloads++;
(function() {
 var loadPackage = function(metadata) {

    var PACKAGE_PATH;
    if (typeof window === 'object') {
      PACKAGE_PATH = window['encodeURIComponent'](window.location.pathname.toString().substring(0, window.location.pathname.toString().lastIndexOf('/')) + '/');
    } else if (typeof location !== 'undefined') {
      // worker
      PACKAGE_PATH = encodeURIComponent(location.pathname.toString().substring(0, location.pathname.toString().lastIndexOf('/')) + '/');
    } else {
      throw 'using preloaded data can only be done on a web page or in a web worker';
    }
    var PACKAGE_NAME = '/home/tom/ab/renpyweb/build/t/pythonhome.data';
    var REMOTE_PACKAGE_BASE = 'pythonhome.data';
    if (typeof Module['locateFilePackage'] === 'function' && !Module['locateFile']) {
      Module['locateFile'] = Module['locateFilePackage'];
      err('warning: you defined Module.locateFilePackage, that has been renamed to Module.locateFile (using your locateFilePackage for now)');
    }
    var REMOTE_PACKAGE_NAME = Module['locateFile'] ? Module['locateFile'](REMOTE_PACKAGE_BASE, '') : REMOTE_PACKAGE_BASE;
  
    var REMOTE_PACKAGE_SIZE = metadata.remote_package_size;
    var PACKAGE_UUID = metadata.package_uuid;
  
    function fetchRemotePackage(packageName, packageSize, callback, errback) {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', packageName, true);
      xhr.responseType = 'arraybuffer';
      xhr.onprogress = function(event) {
        var url = packageName;
        var size = packageSize;
        if (event.total) size = event.total;
        if (event.loaded) {
          if (!xhr.addedTotal) {
            xhr.addedTotal = true;
            if (!Module.dataFileDownloads) Module.dataFileDownloads = {};
            Module.dataFileDownloads[url] = {
              loaded: event.loaded,
              total: size
            };
          } else {
            Module.dataFileDownloads[url].loaded = event.loaded;
          }
          var total = 0;
          var loaded = 0;
          var num = 0;
          for (var download in Module.dataFileDownloads) {
          var data = Module.dataFileDownloads[download];
            total += data.total;
            loaded += data.loaded;
            num++;
          }
          total = Math.ceil(total * Module.expectedDataFileDownloads/num);
          if (Module['setStatus']) Module['setStatus']('Downloading data... (' + loaded + '/' + total + ')');
        } else if (!Module.dataFileDownloads) {
          if (Module['setStatus']) Module['setStatus']('Downloading data...');
        }
      };
      xhr.onerror = function(event) {
        throw new Error("NetworkError for: " + packageName);
      }
      xhr.onload = function(event) {
        if (xhr.status == 200 || xhr.status == 304 || xhr.status == 206 || (xhr.status == 0 && xhr.response)) { // file URLs can return 0
          var packageData = xhr.response;
          callback(packageData);
        } else {
          throw new Error(xhr.statusText + " : " + xhr.responseURL);
        }
      };
      xhr.send(null);
    };

    function handleError(error) {
      console.error('package error:', error);
    };
  
  function runWithFS() {

    function assert(check, msg) {
      if (!check) throw msg + new Error().stack;
    }
Module['FS_createPath']('/', 'lib', true, true);
Module['FS_createPath']('/lib', 'python2.7', true, true);
Module['FS_createPath']('/lib/python2.7', 'importlib', true, true);
Module['FS_createPath']('/lib/python2.7', 'xml', true, true);
Module['FS_createPath']('/lib/python2.7/xml', 'etree', true, true);
Module['FS_createPath']('/lib/python2.7', 'json', true, true);
Module['FS_createPath']('/lib/python2.7', 'encodings', true, true);

    function DataRequest(start, end, audio) {
      this.start = start;
      this.end = end;
      this.audio = audio;
    }
    DataRequest.prototype = {
      requests: {},
      open: function(mode, name) {
        this.name = name;
        this.requests[name] = this;
        Module['addRunDependency']('fp ' + this.name);
      },
      send: function() {},
      onload: function() {
        var byteArray = this.byteArray.subarray(this.start, this.end);
        this.finish(byteArray);
      },
      finish: function(byteArray) {
        var that = this;

        Module['FS_createDataFile'](this.name, null, byteArray, true, true, true); // canOwn this data in the filesystem, it is a slide into the heap that will never change
        Module['removeRunDependency']('fp ' + that.name);

        this.requests[this.name] = null;
      }
    };

        var files = metadata.files;
        for (var i = 0; i < files.length; ++i) {
          new DataRequest(files[i].start, files[i].end, files[i].audio).open('GET', files[i].filename);
        }

  
      var indexedDB = window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || window.msIndexedDB;
      var IDB_RO = "readonly";
      var IDB_RW = "readwrite";
      var DB_NAME = "EM_PRELOAD_CACHE";
      var DB_VERSION = 1;
      var METADATA_STORE_NAME = 'METADATA';
      var PACKAGE_STORE_NAME = 'PACKAGES';
      function openDatabase(callback, errback) {
        try {
          var openRequest = indexedDB.open(DB_NAME, DB_VERSION);
        } catch (e) {
          return errback(e);
        }
        openRequest.onupgradeneeded = function(event) {
          var db = event.target.result;

          if(db.objectStoreNames.contains(PACKAGE_STORE_NAME)) {
            db.deleteObjectStore(PACKAGE_STORE_NAME);
          }
          var packages = db.createObjectStore(PACKAGE_STORE_NAME);

          if(db.objectStoreNames.contains(METADATA_STORE_NAME)) {
            db.deleteObjectStore(METADATA_STORE_NAME);
          }
          var metadata = db.createObjectStore(METADATA_STORE_NAME);
        };
        openRequest.onsuccess = function(event) {
          var db = event.target.result;
          callback(db);
        };
        openRequest.onerror = function(error) {
          errback(error);
        };
      };

      // This is needed as chromium has a limit on per-entry files in IndexedDB
      // https://cs.chromium.org/chromium/src/content/renderer/indexed_db/webidbdatabase_impl.cc?type=cs&sq=package:chromium&g=0&l=177
      // https://cs.chromium.org/chromium/src/out/Debug/gen/third_party/blink/public/mojom/indexeddb/indexeddb.mojom.h?type=cs&sq=package:chromium&g=0&l=60
      // We set the chunk size to 64MB to stay well-below the limit
      var CHUNK_SIZE = 64 * 1024 * 1024;

      function cacheRemotePackage(
        db,
        packageName,
        packageData,
        packageMeta,
        callback,
        errback
      ) {
        var transactionPackages = db.transaction([PACKAGE_STORE_NAME], IDB_RW);
        var packages = transactionPackages.objectStore(PACKAGE_STORE_NAME);
        var chunkSliceStart = 0;
        var nextChunkSliceStart = 0;
        var chunkCount = Math.ceil(packageData.byteLength / CHUNK_SIZE);
        var finishedChunks = 0;
        for (var chunkId = 0; chunkId < chunkCount; chunkId++) {
          nextChunkSliceStart += CHUNK_SIZE;
          var putPackageRequest = packages.put(
            packageData.slice(chunkSliceStart, nextChunkSliceStart),
            'package/' + packageName + '/' + chunkId
          );
          chunkSliceStart = nextChunkSliceStart;
          putPackageRequest.onsuccess = function(event) {
            finishedChunks++;
            if (finishedChunks == chunkCount) {
              var transaction_metadata = db.transaction(
                [METADATA_STORE_NAME],
                IDB_RW
              );
              var metadata = transaction_metadata.objectStore(METADATA_STORE_NAME);
              var putMetadataRequest = metadata.put(
                {
                  uuid: packageMeta.uuid,
                  chunkCount: chunkCount
                },
                'metadata/' + packageName
              );
              putMetadataRequest.onsuccess = function(event) {
                callback(packageData);
              };
              putMetadataRequest.onerror = function(error) {
                errback(error);
              };
            }
          };
          putPackageRequest.onerror = function(error) {
            errback(error);
          };
        }
      }

      /* Check if there's a cached package, and if so whether it's the latest available */
      function checkCachedPackage(db, packageName, callback, errback) {
        var transaction = db.transaction([METADATA_STORE_NAME], IDB_RO);
        var metadata = transaction.objectStore(METADATA_STORE_NAME);
        var getRequest = metadata.get('metadata/' + packageName);
        getRequest.onsuccess = function(event) {
          var result = event.target.result;
          if (!result) {
            return callback(false, null);
          } else {
            return callback(PACKAGE_UUID === result.uuid, result);
          }
        };
        getRequest.onerror = function(error) {
          errback(error);
        };
      }

      function fetchCachedPackage(db, packageName, metadata, callback, errback) {
        var transaction = db.transaction([PACKAGE_STORE_NAME], IDB_RO);
        var packages = transaction.objectStore(PACKAGE_STORE_NAME);

        var chunksDone = 0;
        var totalSize = 0;
        var chunks = new Array(metadata.chunkCount);

        for (var chunkId = 0; chunkId < metadata.chunkCount; chunkId++) {
          var getRequest = packages.get('package/' + packageName + '/' + chunkId);
          getRequest.onsuccess = function(event) {
            // If there's only 1 chunk, there's nothing to concatenate it with so we can just return it now
            if (metadata.chunkCount == 1) {
              callback(event.target.result);
            } else {
              chunksDone++;
              totalSize += event.target.result.byteLength;
              chunks.push(event.target.result);
              if (chunksDone == metadata.chunkCount) {
                if (chunksDone == 1) {
                  callback(event.target.result);
                } else {
                  var tempTyped = new Uint8Array(totalSize);
                  var byteOffset = 0;
                  for (var chunkId in chunks) {
                    var buffer = chunks[chunkId];
                    tempTyped.set(new Uint8Array(buffer), byteOffset);
                    byteOffset += buffer.byteLength;
                    buffer = undefined;
                  }
                  chunks = undefined;
                  callback(tempTyped.buffer);
                  tempTyped = undefined;
                }
              }
            }
          };
          getRequest.onerror = function(error) {
            errback(error);
          };
        }
      }
    
    function processPackageData(arrayBuffer) {
      Module.finishedDataFileDownloads++;
      assert(arrayBuffer, 'Loading data file failed.');
      assert(arrayBuffer instanceof ArrayBuffer, 'bad input to processPackageData');
      var byteArray = new Uint8Array(arrayBuffer);
      var curr;
      
        // Reuse the bytearray from the XHR as the source for file reads.
        DataRequest.prototype.byteArray = byteArray;
  
          var files = metadata.files;
          for (var i = 0; i < files.length; ++i) {
            DataRequest.prototype.requests[files[i].filename].onload();
          }
              Module['removeRunDependency']('datafile_/home/tom/ab/renpyweb/build/t/pythonhome.data');

    };
    Module['addRunDependency']('datafile_/home/tom/ab/renpyweb/build/t/pythonhome.data');
  
    if (!Module.preloadResults) Module.preloadResults = {};
  
      function preloadFallback(error) {
        console.error(error);
        console.error('falling back to default preload behavior');
        fetchRemotePackage(REMOTE_PACKAGE_NAME, REMOTE_PACKAGE_SIZE, processPackageData, handleError);
      };

      openDatabase(
        function(db) {
          checkCachedPackage(db, PACKAGE_PATH + PACKAGE_NAME,
            function(useCached, metadata) {
              Module.preloadResults[PACKAGE_NAME] = {fromCache: useCached};
              if (useCached) {
                console.info('loading ' + PACKAGE_NAME + ' from cache');
                fetchCachedPackage(db, PACKAGE_PATH + PACKAGE_NAME, metadata, processPackageData, preloadFallback);
              } else {
                console.info('loading ' + PACKAGE_NAME + ' from remote');
                fetchRemotePackage(REMOTE_PACKAGE_NAME, REMOTE_PACKAGE_SIZE,
                  function(packageData) {
                    cacheRemotePackage(db, PACKAGE_PATH + PACKAGE_NAME, packageData, {uuid:PACKAGE_UUID}, processPackageData,
                      function(error) {
                        console.error(error);
                        processPackageData(packageData);
                      });
                  }
                , preloadFallback);
              }
            }
          , preloadFallback);
        }
      , preloadFallback);

      if (Module['setStatus']) Module['setStatus']('Downloading...');
    
  }
  if (Module['calledRun']) {
    runWithFS();
  } else {
    if (!Module['preRun']) Module['preRun'] = [];
    Module["preRun"].push(runWithFS); // FS is not initialized yet, wait for it
  }

 }
 loadPackage({"files": [{"start": 0, "audio": 0, "end": 41200, "filename": "/lib/python2.7/zipfile.pyo"}, {"start": 41200, "audio": 0, "end": 44662, "filename": "/lib/python2.7/genericpath.pyo"}, {"start": 44662, "audio": 0, "end": 49962, "filename": "/lib/python2.7/repr.pyo"}, {"start": 49962, "audio": 0, "end": 58557, "filename": "/lib/python2.7/UserDict.pyo"}, {"start": 58557, "audio": 0, "end": 78266, "filename": "/lib/python2.7/tempfile.pyo"}, {"start": 78266, "audio": 0, "end": 90594, "filename": "/lib/python2.7/sre_compile.pyo"}, {"start": 90594, "audio": 0, "end": 94178, "filename": "/lib/python2.7/fnmatch.pyo"}, {"start": 94178, "audio": 0, "end": 96273, "filename": "/lib/python2.7/keyword.pyo"}, {"start": 96273, "audio": 0, "end": 109581, "filename": "/lib/python2.7/re.pyo"}, {"start": 109581, "audio": 0, "end": 146326, "filename": "/lib/python2.7/platform.pyo"}, {"start": 146326, "audio": 0, "end": 164544, "filename": "/lib/python2.7/shutil.pyo"}, {"start": 164544, "audio": 0, "end": 179887, "filename": "/lib/python2.7/gettext.pyo"}, {"start": 179887, "audio": 0, "end": 219533, "filename": "/lib/python2.7/inspect.pyo"}, {"start": 219533, "audio": 0, "end": 231112, "filename": "/lib/python2.7/traceback.pyo"}, {"start": 231112, "audio": 0, "end": 251146, "filename": "/lib/python2.7/webbrowser.pyo"}, {"start": 251146, "audio": 0, "end": 276176, "filename": "/lib/python2.7/_abcoll.pyo"}, {"start": 276176, "audio": 0, "end": 287561, "filename": "/lib/python2.7/StringIO.pyo"}, {"start": 287561, "audio": 0, "end": 295039, "filename": "/lib/python2.7/shlex.pyo"}, {"start": 295039, "audio": 0, "end": 369641, "filename": "/lib/python2.7/tarfile.pyo"}, {"start": 369641, "audio": 0, "end": 387005, "filename": "/lib/python2.7/sysconfig.pyo"}, {"start": 387005, "audio": 0, "end": 390247, "filename": "/lib/python2.7/linecache.pyo"}, {"start": 390247, "audio": 0, "end": 402189, "filename": "/lib/python2.7/copy.pyo"}, {"start": 402189, "audio": 0, "end": 416276, "filename": "/lib/python2.7/tokenize.pyo"}, {"start": 416276, "audio": 0, "end": 420227, "filename": "/lib/python2.7/colorsys.pyo"}, {"start": 420227, "audio": 0, "end": 424420, "filename": "/lib/python2.7/__future__.pyo"}, {"start": 424420, "audio": 0, "end": 427121, "filename": "/lib/python2.7/stat.pyo"}, {"start": 427121, "audio": 0, "end": 427355, "filename": "/lib/python2.7/struct.pyo"}, {"start": 427355, "audio": 0, "end": 433281, "filename": "/lib/python2.7/functools.pyo"}, {"start": 433281, "audio": 0, "end": 447756, "filename": "/lib/python2.7/heapq.pyo"}, {"start": 447756, "audio": 0, "end": 511167, "filename": "/lib/python2.7/argparse.pyo"}, {"start": 511167, "audio": 0, "end": 513857, "filename": "/lib/python2.7/types.pyo"}, {"start": 513857, "audio": 0, "end": 520721, "filename": "/lib/python2.7/hashlib.pyo"}, {"start": 520721, "audio": 0, "end": 539876, "filename": "/lib/python2.7/_sysconfigdata.pyo"}, {"start": 539876, "audio": 0, "end": 551618, "filename": "/lib/python2.7/textwrap.pyo"}, {"start": 551618, "audio": 0, "end": 557788, "filename": "/lib/python2.7/sre_constants.pyo"}, {"start": 557788, "audio": 0, "end": 594027, "filename": "/lib/python2.7/codecs.pyo"}, {"start": 594027, "audio": 0, "end": 606188, "filename": "/lib/python2.7/warnings.pyo"}, {"start": 606188, "audio": 0, "end": 626392, "filename": "/lib/python2.7/string.pyo"}, {"start": 626392, "audio": 0, "end": 639210, "filename": "/lib/python2.7/ast.pyo"}, {"start": 639210, "audio": 0, "end": 650008, "filename": "/lib/python2.7/base64.pyo"}, {"start": 650008, "audio": 0, "end": 664395, "filename": "/lib/python2.7/urlparse.pyo"}, {"start": 664395, "audio": 0, "end": 689819, "filename": "/lib/python2.7/os.pyo"}, {"start": 689819, "audio": 0, "end": 695939, "filename": "/lib/python2.7/opcode.pyo"}, {"start": 695939, "audio": 0, "end": 721249, "filename": "/lib/python2.7/collections.pyo"}, {"start": 721249, "audio": 0, "end": 782822, "filename": "/lib/python2.7/difflib.pyo"}, {"start": 782822, "audio": 0, "end": 808177, "filename": "/lib/python2.7/random.pyo"}, {"start": 808177, "audio": 0, "end": 813496, "filename": "/lib/python2.7/dummy_thread.pyo"}, {"start": 813496, "audio": 0, "end": 819684, "filename": "/lib/python2.7/dis.pyo"}, {"start": 819684, "audio": 0, "end": 824679, "filename": "/lib/python2.7/copy_reg.pyo"}, {"start": 824679, "audio": 0, "end": 839773, "filename": "/lib/python2.7/weakref.pyo"}, {"start": 839773, "audio": 0, "end": 858810, "filename": "/lib/python2.7/site.pyo"}, {"start": 858810, "audio": 0, "end": 878647, "filename": "/lib/python2.7/sre_parse.pyo"}, {"start": 878647, "audio": 0, "end": 933549, "filename": "/lib/python2.7/locale.pyo"}, {"start": 933549, "audio": 0, "end": 937112, "filename": "/lib/python2.7/io.pyo"}, {"start": 937112, "audio": 0, "end": 974868, "filename": "/lib/python2.7/pickle.pyo"}, {"start": 974868, "audio": 0, "end": 978659, "filename": "/lib/python2.7/token.pyo"}, {"start": 978659, "audio": 0, "end": 984691, "filename": "/lib/python2.7/abc.pyo"}, {"start": 984691, "audio": 0, "end": 995996, "filename": "/lib/python2.7/posixpath.pyo"}, {"start": 995996, "audio": 0, "end": 998899, "filename": "/lib/python2.7/glob.pyo"}, {"start": 998899, "audio": 0, "end": 1008337, "filename": "/lib/python2.7/_weakrefset.pyo"}, {"start": 1008337, "audio": 0, "end": 1012731, "filename": "/lib/python2.7/contextlib.pyo"}, {"start": 1012731, "audio": 0, "end": 1014218, "filename": "/lib/python2.7/importlib/__init__.pyo"}, {"start": 1014218, "audio": 0, "end": 1015291, "filename": "/lib/python2.7/xml/__init__.pyo"}, {"start": 1015291, "audio": 0, "end": 1015415, "filename": "/lib/python2.7/xml/etree/__init__.pyo"}, {"start": 1015415, "audio": 0, "end": 1049395, "filename": "/lib/python2.7/xml/etree/ElementTree.pyo"}, {"start": 1049395, "audio": 0, "end": 1056888, "filename": "/lib/python2.7/xml/etree/ElementPath.pyo"}, {"start": 1056888, "audio": 0, "end": 1070513, "filename": "/lib/python2.7/json/encoder.pyo"}, {"start": 1070513, "audio": 0, "end": 1084443, "filename": "/lib/python2.7/json/__init__.pyo"}, {"start": 1084443, "audio": 0, "end": 1096478, "filename": "/lib/python2.7/json/decoder.pyo"}, {"start": 1096478, "audio": 0, "end": 1098692, "filename": "/lib/python2.7/json/scanner.pyo"}, {"start": 1098692, "audio": 0, "end": 1100875, "filename": "/lib/python2.7/encodings/raw_unicode_escape.pyo"}, {"start": 1100875, "audio": 0, "end": 1105304, "filename": "/lib/python2.7/encodings/zlib_codec.pyo"}, {"start": 1105304, "audio": 0, "end": 1107535, "filename": "/lib/python2.7/encodings/ascii.pyo"}, {"start": 1107535, "audio": 0, "end": 1111893, "filename": "/lib/python2.7/encodings/__init__.pyo"}, {"start": 1111893, "audio": 0, "end": 1113760, "filename": "/lib/python2.7/encodings/utf_32_be.pyo"}, {"start": 1113760, "audio": 0, "end": 1116021, "filename": "/lib/python2.7/encodings/latin_1.pyo"}, {"start": 1116021, "audio": 0, "end": 1119586, "filename": "/lib/python2.7/encodings/hex_codec.pyo"}, {"start": 1119586, "audio": 0, "end": 1128351, "filename": "/lib/python2.7/encodings/aliases.pyo"}, {"start": 1128351, "audio": 0, "end": 1130277, "filename": "/lib/python2.7/encodings/utf_8.pyo"}], "remote_package_size": 1130277, "package_uuid": "ee728627-6c3f-45ad-9c6c-efcf9c14fb84"});

})();

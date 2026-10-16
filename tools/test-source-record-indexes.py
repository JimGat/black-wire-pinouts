"""Source-only references get native pages without inflating saved-file counts."""
import contextlib,io,json,pathlib,runpy,sys,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
class SourceRecordIndexTest(unittest.TestCase):
 def test_linked_hardware_pages_are_indexed_without_becoming_saved_files(self):
  ns=runpy.run_path(str(ROOT/'tools/rebuild-indexes.py'))
  with tempfile.TemporaryDirectory() as folder:
   root=pathlib.Path(folder);lib=root/'library';lib.mkdir();(root/'catalog').mkdir()
   (root/'catalog/board-paths.json').write_text('{}')
   asset={'id':'a','file':'media/a.png','bytes':1,'hash':'a'*64,'label':'Saved reference','type':'board photograph','review':'Source recorded','extension':'png','rights':'Test fixture','sources':[]}
   base={'brand':'Example','processor':'ESP32-C5','family':'CYD','revision':'Unknown','coverage':'Source-only evidence','pinouts':0,'sources':[]}
   source={**base,'id':'source','name':'Source-linked host','assets':[],'documentation':{'resources':[{'kind':'hardware-guide','scope':'board','url':'https://example.com/manual','label':'Hardware manual'}]},'documentationCoverage':{'boardDatasheets':0,'visualCount':0},'pinReferences':[{'connector':'Source function table','scope':'Functions only','orientation':'Physical order unverified','source':{'url':'https://example.com/manual','locator':'Pin table'},'review':'Not bench tested','pins':[{'label':'GPIO6','purpose':'SPI clock','notes':'No physical map claimed'}]}]}
   c={'boards':[{**base,'id':'saved','name':'Saved board','assets':[asset]},source], 'stats':{},'deviceWatchlist':[]}
   (lib/'catalog.json').write_text(json.dumps(c))
   ns['main'].__globals__.update(ROOT=root,LIB=lib)
   old=sys.argv;sys.argv=['rebuild-indexes.py']
   try:
    with contextlib.redirect_stdout(io.StringIO()):ns['main']()
   finally:sys.argv=old
   paths=json.loads((root/'catalog/board-paths.json').read_text())
   self.assertIn('source',paths)
   page=(root/paths['source']).read_text();self.assertIn('Hardware manual',page);self.assertIn('SPI clock',page)
   self.assertIn('Source-linked host',(root/'BROWSE.md').read_text())
   result=json.loads((lib/'catalog.json').read_text());self.assertEqual(result['stats']['boardsWithFiles'],1);self.assertEqual(result['stats']['referenceEntries'],1)
if __name__=='__main__':unittest.main()

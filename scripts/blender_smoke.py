"""Run only in Blender. Render the unmodified factory scene on the CPU."""
import bpy, json, time
from pathlib import Path
root = Path(__file__).resolve().parents[1]
out = root / 'evidence' / 'environment' / 'blender-smoke'
out.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=False)
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 8
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = str(out / 'default-scene.png')
scene.render.film_transparent = False
bpy.ops.wm.save_as_mainfile(filepath=str(out / 'default-scene.blend'))
start = time.perf_counter()
bpy.ops.render.render(write_still=True)
result = {'status':'passed','blenderVersion':bpy.app.version_string,'renderSeconds':round(time.perf_counter()-start,3),'engine':'CYCLES','device':'CPU','resolution':[1280,720],'scene':'unmodified factory cube, camera and light','image':'blender-smoke/default-scene.png','modelAuthor':'Blender factory scene; no project model created'}
(out.parent / 'blender-render.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

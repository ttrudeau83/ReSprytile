### BLENDER 5.x NOTICE:
Version 1.1.0 is updated for Blender 5.x (tested on Blender 5.2 on Windows). It requires Blender 5.0 or newer;
use an older release for Blender 4.x. If you see anything misbehaving, please submit an issue.


<p align="center">
    <img src="sprytile-logo.png?raw=true" height="100px"/>
    <h1 align="center">ReSprytile</h1>
    <h2 align="center">Fork of Sprytile Painter</h2>
    <h3 align="center">Updated for Blender 5.x</h3>
    <h4 align="center">
        A <img src="https://download.blender.org/institute/logos/blender-socket.png" height="20px"/> addon for creating tile based low spec 3D scenes. (Unofficial port for Blender 5.x)
    </h4>
  <br>
</p>

### Features

* Tile building: Build your mesh directly with tiles, skip tedious UV mapping while quickly rotating and flipping tiles.
* UV painting: Create your mesh with other Blender tools, then quickly UV map them to your tiles. Spend less time in the UV editor.
* Pixel grid tools: Keep your mesh aligned to the grid with pixel translation, move vertices around with confidence.

### Demo:

![Timelapse](https://img.itch.io/aW1hZ2UvOTg5NjYvNTE3NTczLmdpZg==/250x600/mDFwN0.gif)

### Download:

Download from [releases](https://github.com/ttrudeau83/ReSprytile/releases), then in Blender use
*Edit > Preferences > Add-ons > Install from Disk* and pick the zip.
Installing a new version over an old one takes effect right away, no restart needed.

### Getting Started:

1. Select a mesh object and open the 3D Viewport sidebar (**N**), **Sprytile** tab.
2. In Object Mode, use **Load Tileset** or **Add Tileset** in the *Material Setup* box to pick your sprite sheet (any PNG).
   In Edit Mode the same *Add Tileset* is in the **▼** menu next to the grid list, and **+** opens it when no tileset is loaded yet.
3. Set **Grid Size** to your tile size (e.g. 8x8).
4. Press **Tab** for Edit Mode, pick the Sprytile Paint/Build tool from the toolbar and click tiles in the palette.

Painting fits exactly one tile onto each face (**Stretch X/Y**, on by default). Turn Stretch off to map tiles at world
scale instead, using **World Pixels** (pixels per Blender unit).

* [Sprytile Basics Tutorial](http://docs.sprytile.xyz/quick-start/) ([video](https://youtu.be/-ezYZgMp-R0))

### Community:

* Chat with the fellow users in the [Discord server](http://discord.sprytile.xyz/)
* Showcase your work or ask for support in the [forum](https://chemikhazi.itch.io/sprytile/community)

### Issue/Feature requests:
Bug reports for this port can be submitted to [GitHub issues](https://github.com/ttrudeau83/ReSprytile/issues)

### Blender 5.x changes (1.1.0)
* Removed the `bgl` module and legacy shader API (both removed in Blender 5.0); the GUI uses the `gpu` module on all platforms.
* Fixed crashes/errors from Blender 5.0's separation of ID properties and `bpy.props` (paint alignment, work layer, preferences).
* Tile palette: crisp pixel sampling, tileset fills the palette (correct tile picking and preview), kept clear of the toolbar/sidebar.
* Painting faces viewed at an angle no longer squashes the tile; Stretch X/Y on by default.
* Reinstalling/re-enabling the add-on reloads its code without restarting Blender.

### Acknowledgments:

The bulk of Blender 2.8 porting work by was done by [Yonnji](https://github.com/Yonnji) and [ologon](https://github.com/ologon), with additional contributions by [brandy92](https://github.com/brandy92). 
The bulk of the Blender 3.x porting work was done by [IonTheDev](https://github.com/IonTheDev). 
The bulk of the Blender 4.x porting was done by [Taron686](https://github.com/Taron686)
The Blender 5.x port is maintained at [ttrudeau83/ReSprytile](https://github.com/ttrudeau83/ReSprytile).



I simply just picked up the torch for this project, Python is not my native language and I am learning it as I develope this fork. 

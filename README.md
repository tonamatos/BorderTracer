# BorderTracer

Border tracing is an important segmentation method for two-dimensional digital image processing which determines the frontiers of objects. Boundary tracing algorithms are commonly first formulated for binary images where the object points have a special value in the image, while all other points, called _background points_, have another value. These algorithms are later combined with methods of object detection, such as filtering, edge detection or texture recognition. The _boundary_ of an object is expected to separate the object from the background, a contour is commonly a path of boundary elements.

The generalization from square pixels, which constitute the standard for 2D digital images, to polygonal tiles is justified by the notable attention that polygonal tilings, particularly rectangular, triangular and hexagonal tilings, have received for several decades as alternative model to 2D digital images. Such tilings have been employed, for example, to study the preservation of topological properties during thinning. Rectangular and triangular tilings are special cases of the polygonal tilings used to analyse convexity properties of digital objects and to develop its representation via the minimal perimeter polygon. Triangular and hexagonal pixels have been explicitly employed, for example, in the following:

  - to develop tools for image processing and image modelling;
  
  - to design thinning algorithms that preserve topological and geometrical properties of the objects of interest;

  - to perform geometrical transformations, to define geometrical figures such as straight lines or circular arcs, and to study shortest paths;
  
  - to design digital distance functions with applications in distance transformations employed for skeletonization;

  - special coordinate systems to handle triangular and hexagonal pixels were proposed;
  
  - triangular pixels were suggested for graphical data visualization; and
  
  - representations of objects in digital images as unions of polygonal tiles, independently from the "geometrical form" of the pixels, can be useful in the classification or recognition of the objects.
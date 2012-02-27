# -*- coding: utf-8 -*-
#
#
#int ImagingNewCount = 0;
#
#/* --------------------------------------------------------------------
# * Standard image object.
# */
#
#Imaging
#ImagingNewPrologueSubtype(const char *mode, unsigned xsize, unsigned ysize,
#                          int size)
#{
#    Imaging im;
#    ImagingSectionCookie cookie;
#
#    im = (Imaging) calloc(1, size);
#    if (!im)
#    return (Imaging) ImagingError_MemoryError();
#
#    /* Setup image descriptor */
#    im->xsize = xsize;
#    im->ysize = ysize;
#
#    im->type = IMAGING_TYPE_UINT8;
#
#    if (strcmp(mode, "1") == 0) {
#        /* 1-bit images */
#        im->bands = im->pixelsize = 1;
#        im->linesize = xsize;
#
#    } else if (strcmp(mode, "P") == 0) {
#        /* 8-bit palette mapped images */
#        im->bands = im->pixelsize = 1;
#        im->linesize = xsize;
#        im->palette = ImagingPaletteNew("RGB");
#
#    } else if (strcmp(mode, "PA") == 0) {
#        /* 8-bit palette with alpha */
#        im->bands = 2;
#        im->pixelsize = 4; /* store in image32 memory */
#        im->linesize = xsize * 4;
#        im->palette = ImagingPaletteNew("RGB");
#
#    } else if (strcmp(mode, "L") == 0) {
#        /* 8-bit greyscale (luminance) images */
#        im->bands = im->pixelsize = 1;
#        im->linesize = xsize;
#
#    } else if (strcmp(mode, "LA") == 0) {
#        /* 8-bit greyscale (luminance) with alpha */
#        im->bands = 2;
#        im->pixelsize = 4; /* store in image32 memory */
#        im->linesize = xsize * 4;
#
#    } else if (strcmp(mode, "F") == 0) {
#        /* 32-bit floating point images */
#        im->bands = 1;
#        im->pixelsize = 4;
#        im->linesize = xsize * 4;
#        im->type = IMAGING_TYPE_FLOAT32;
#
#    } else if (strcmp(mode, "I") == 0) {
#        /* 32-bit integer images */
#        im->bands = 1;
#        im->pixelsize = 4;
#        im->linesize = xsize * 4;
#        im->type = IMAGING_TYPE_INT32;
#
#    } else if (strcmp(mode, "I;16") == 0 || strcmp(mode, "I;16L") == 0 || strcmp(mode, "I;16B") == 0) {
#        /* EXPERIMENTAL */
#        /* 16-bit raw integer images */
#        im->bands = 1;
#        im->pixelsize = 2;
#        im->linesize = xsize * 2;
#        im->type = IMAGING_TYPE_SPECIAL;
#
#    } else if (strcmp(mode, "RGB") == 0) {
#        /* 24-bit true colour images */
#        im->bands = 3;
#        im->pixelsize = 4;
#        im->linesize = xsize * 4;
#
#    } else if (strcmp(mode, "BGR;15") == 0) {
#        /* EXPERIMENTAL */
#        /* 15-bit true colour */
#        im->bands = 1;
#        im->pixelsize = 2;
#        im->linesize = (xsize*2 + 3) & -4;
#        im->type = IMAGING_TYPE_SPECIAL;
#
#    } else if (strcmp(mode, "BGR;16") == 0) {
#        /* EXPERIMENTAL */
#        /* 16-bit reversed true colour */
#        im->bands = 1;
#        im->pixelsize = 2;
#        im->linesize = (xsize*2 + 3) & -4;
#        im->type = IMAGING_TYPE_SPECIAL;
#
#    } else if (strcmp(mode, "BGR;24") == 0) {
#        /* EXPERIMENTAL */
#        /* 24-bit reversed true colour */
#        im->bands = 1;
#        im->pixelsize = 3;
#        im->linesize = (xsize*3 + 3) & -4;
#        im->type = IMAGING_TYPE_SPECIAL;
#
#    } else if (strcmp(mode, "BGR;32") == 0) {
#        /* EXPERIMENTAL */
#        /* 32-bit reversed true colour */
#        im->bands = 1;
#        im->pixelsize = 4;
#        im->linesize = (xsize*4 + 3) & -4;
#        im->type = IMAGING_TYPE_SPECIAL;
#
#    } else if (strcmp(mode, "RGBX") == 0) {
#        /* 32-bit true colour images with padding */
#        im->bands = im->pixelsize = 4;
#        im->linesize = xsize * 4;
#
#    } else if (strcmp(mode, "RGBA") == 0) {
#        /* 32-bit true colour images with alpha */
#        im->bands = im->pixelsize = 4;
#        im->linesize = xsize * 4;
#
#    } else if (strcmp(mode, "RGBa") == 0) {
#        /* EXPERIMENTAL */
#        /* 32-bit true colour images with premultiplied alpha */
#        im->bands = im->pixelsize = 4;
#        im->linesize = xsize * 4;
#
#    } else if (strcmp(mode, "CMYK") == 0) {
#        /* 32-bit colour separation */
#        im->bands = im->pixelsize = 4;
#        im->linesize = xsize * 4;
#
#    } else if (strcmp(mode, "YCbCr") == 0) {
#        /* 24-bit video format */
#        im->bands = 3;
#        im->pixelsize = 4;
#        im->linesize = xsize * 4;
#
#    } else {
#        free(im);
#    return (Imaging) ImagingError_ValueError("unrecognized mode");
#    }
#
#    /* Setup image descriptor */
#    strcpy(im->mode, mode);
#
#    ImagingSectionEnter(&cookie);
#
#    /* Pointer array (allocate at least one line, to avoid MemoryError
#       exceptions on platforms where calloc(0, x) returns NULL) */
#    im->image = (char **) calloc((ysize > 0) ? ysize : 1, sizeof(void *));
#
#    ImagingSectionLeave(&cookie);
#
#    if (!im->image) {
#    free(im);
#    return (Imaging) ImagingError_MemoryError();
#    }
#
#    ImagingNewCount++;
#
#    return im;
#}
#
#Imaging
#ImagingNewPrologue(const char *mode, unsigned xsize, unsigned ysize)
#{
#    return ImagingNewPrologueSubtype(
#        mode, xsize, ysize, sizeof(struct ImagingMemoryInstance)
#        );
#}
#
#Imaging
#ImagingNewEpilogue(Imaging im)
#{
#    /* If the raster data allocator didn't setup a destructor,
#       assume that it couldn't allocate the required amount of
#       memory. */
#    if (!im->destroy)
#    return (Imaging) ImagingError_MemoryError();
#
#    /* Initialize alias pointers to pixel data. */
#    switch (im->pixelsize) {
#    case 1: case 2: case 3:
#    im->image8 = (UINT8 **) im->image;
#    break;
#    case 4:
#    im->image32 = (INT32 **) im->image;
#    break;
#    }
#
#    return im;
#}
#
#void
#ImagingDelete(Imaging im)
#{
#    if (!im)
#    return;
#
#    if (im->palette)
#    ImagingPaletteDelete(im->palette);
#
#    if (im->destroy)
#    im->destroy(im);
#
#    if (im->image)
#    free(im->image);
#
#    free(im);
#}
#
#
#/* Array Storage Type */
#/* ------------------ */
#/* Allocate image as an array of line buffers. */
#
#static void
#ImagingDestroyArray(Imaging im)
#{
#    int y;
#
#    if (im->image)
#    for (y = 0; y < im->ysize; y++)
#        if (im->image[y])
#        free(im->image[y]);
#}
#
#Imaging
#ImagingNewArray(const char *mode, int xsize, int ysize)
#{
#    Imaging im;
#    ImagingSectionCookie cookie;
#
#    int y;
#    char* p;
#
#    im = ImagingNewPrologue(mode, xsize, ysize);
#    if (!im)
#    return NULL;
#
#    ImagingSectionEnter(&cookie);
#
#    /* Allocate image as an array of lines */
#    for (y = 0; y < im->ysize; y++) {
#    p = (char *) malloc(im->linesize);
#    if (!p) {
#        ImagingDestroyArray(im);
#        break;
#    }
#        im->image[y] = p;
#    }
#
#    ImagingSectionLeave(&cookie);
#
#    if (y == im->ysize)
#    im->destroy = ImagingDestroyArray;
#
#    return ImagingNewEpilogue(im);
#}
#
#
#/* Block Storage Type */
#/* ------------------ */
#/* Allocate image as a single block. */
#
#static void
#ImagingDestroyBlock(Imaging im)
#{
#    if (im->block)
#    free(im->block);
#}
#
#Imaging
#ImagingNewBlock(const char *mode, int xsize, int ysize)
#{
#    Imaging im;
#    int y, i;
#    int bytes;
#
#    im = ImagingNewPrologue(mode, xsize, ysize);
#    if (!im)
#    return NULL;
#
#    /* Use a single block */
#    bytes = im->ysize * im->linesize;
#    if (bytes <= 0)
#        /* some platforms return NULL for malloc(0); this fix
#           prevents MemoryError on zero-sized images on such
#           platforms */
#        bytes = 1;
#    im->block = (char *) malloc(bytes);
#
#    if (im->block) {
#
#    for (y = i = 0; y < im->ysize; y++) {
#        im->image[y] = im->block + i;
#        i += im->linesize;
#    }
#
#    im->destroy = ImagingDestroyBlock;
#
#    }
#
#    return ImagingNewEpilogue(im);
#}
#
#/* --------------------------------------------------------------------
# * Create a new, internally allocated, image.
# */
##if defined(IMAGING_SMALL_MODEL)
##define    THRESHOLD    16384L
##else
##define    THRESHOLD    (2048*2048*4L)
##endif
#
#Imaging
#ImagingNew(const char* mode, int xsize, int ysize)
#{
#    int bytes;
#    Imaging im;
#
#    if (strlen(mode) == 1) {
#        if (mode[0] == 'F' || mode[0] == 'I')
#            bytes = 4;
#        else
#            bytes = 1;
#    } else
#        bytes = strlen(mode); /* close enough */
#
#    if ((long) xsize * ysize * bytes <= THRESHOLD) {
#        im = ImagingNewBlock(mode, xsize, ysize);
#        if (im)
#            return im;
#        /* assume memory error; try allocating in array mode instead */
#        ImagingError_Clear();
#    }
#
#    return ImagingNewArray(mode, xsize, ysize);
#}
#
#Imaging
#ImagingNew2(const char* mode, Imaging imOut, Imaging imIn)
#{
#    /* allocate or validate output image */
#
#    if (imOut) {
#        /* make sure images match */
#        if (strcmp(imOut->mode, mode) != 0
#            || imOut->xsize != imIn->xsize
#            || imOut->ysize != imIn->ysize) {
#            return ImagingError_Mismatch();
#        }
#    } else {
#        /* create new image */
#        imOut = ImagingNew(mode, imIn->xsize, imIn->ysize);
#        if (!imOut)
#            return NULL;
#    }
#
#    return imOut;
#}
#
#void
#ImagingCopyInfo(Imaging destination, Imaging source)
#{
from copy import deepcopy
def copy_info(destination, source):
#    if (source->palette) {
    if source.palette:
#        if (destination->palette)
        if destination.palette:
#            ImagingPaletteDelete(destination->palette);
            del destination.palette
#    destination->palette = ImagingPaletteDuplicate(source->palette);
    destination.palette = deepcopy(source.palette)
#    }
#}
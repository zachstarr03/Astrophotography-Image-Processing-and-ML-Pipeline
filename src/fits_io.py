from astropy.io import fits
import numpy as np

'''
Loads a FITS file and returns: 
1.) data - 2D numpy array of pixel values
2.) header - FITS header object containing metadata
'''
def load_fits(fits_image_filename):

    # parameter "memmap=True" for large files (reads portions of the data into memory only as needed)
    with fits.open(fits_image_filename) as hdul:
        print(hdul.info())
        image_data = hdul[0].data
        header_info = hdul[0].header

        # image_data.dtype = ">f4": float of 4 bytes -> float32 (32-bit floating-point array)
        # convert to native-endian to speed up math for later
        image_data = image_data.astype(np.float32, copy=False)
        print(image_data.dtype)
        print(header_info)

        '''
        # Debug
        print(image_data)
        print(type(image_data))
        print(image_data.dtype)
        print(image_data.shape)
        #print(header_info)
        print(type(header_info))
        print(header_info.get("EXPTIME"))       # exposure time (s)
        '''

    return image_data, header_info

if __name__ == "__main__":
    fits_image_filename = "../data/raw/M51_01.fits"
    #fits_image_filename = "../data/raw/M51_02.fits"

    load_fits(fits_image_filename)

# hudl.info() outputs the dimensions as (8600, 12200) -> (columns, rows)
# image_data.shape: numpy outputs the dimensions as (12200, 8600) -> (rows, columns)





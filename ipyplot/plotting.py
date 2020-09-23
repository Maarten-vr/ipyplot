import numpy as np
from typing import Sequence
from PIL import Image

from .html_helpers import (
    display_html, create_tabs, create_imgs_grid)
from .utils import get_class_representations


def plot_class_tabs(
        images: Sequence[object],
        labels: Sequence[str or int],
        max_imgs_per_tab: int = 15,
        img_width: int = 150,
        zoom_scale: float = 2.5,
        force_b64: bool = False,
        tabs_order: Sequence[str or int] = None):
    """
    Efficient and convenient way of displaying images in interactive tabs
    grouped by labels/clusters.
    It's using IPython.display function and HTML under the hood

    Args:
        images (numpy.ndarray):
            Numpy array of image file paths or PIL.Image objects
        labels (numpy.ndarray):
            Numpy array of corresponding classes
        max_imgs_per_tab (int, optional):
            How many samples from each cluster/class to display.
            Defaults to 15.
        img_width (int, optional):
            Image width.
            Adjust to change the number of images per row.
            Defaults to 150.
        zoom_scale (float, optional):
            Scale for zoom-in-on-click feature.
            Best to keep between 1.0~5.0.
            Defaults to 2.5.
        force_b64 (boolean, optional):
            You can force conversion of images to base64 instead of reading them directly from filepaths with HTML.  # NOQA E501
            Do mind that using b64 conversion vs reading directly from filepath will be slower.  # NOQA E501
            You might need to set this to `True` in environments like Google colab.
            Defaults to False.
    """
    assert(len(images) == len(labels))

    # this is a hack to make the code work with PIL images
    if issubclass(type(images[0]), Image.Image):
        images = np.asarray(images, dtype=type(images[0]))
    else:
        images = np.asarray(images)
    labels = np.asarray(labels)
    # ignore_list = np.asarray(ignore_list) if ignore_list is not None else ignore_list  # NOQA E501
    tabs_order = np.asarray(tabs_order) if tabs_order is not None else tabs_order  # NOQA E501

    html = create_tabs(
        images, labels, max_imgs_per_tab, img_width,
        zoom_scale=zoom_scale, force_b64=force_b64, tabs_order=tabs_order)

    display_html(html)


def plot_images(
        images: Sequence[object],
        labels: Sequence[str or int] = None,
        max_images=30,
        img_width: int = 150,
        zoom_scale: float = 2.5,
        force_b64: bool = False):
    """
    Displays images based on the provided paths

    Args:
        images (array):
            Array of coresponding file paths.
        labels (array, optional):
            Array of labels/cluster names.
            If None it will just assign numbers going from 0
            Defaults to None.
        max_images (int, optional):
            Max number of images to display.
            Defaults to 30.
        img_width (int, optional):
            Width of the displayed image.
            Defaults to 150.
        zoom_scale (float, optional):
            Scale for zoom-in-on-click feature.
            Best to keep between 1.0~5.0.
            Defaults to 2.5.
        force_b64 (boolean, optional):
            You can force conversion of images to base64 instead of reading them directly from filepaths with HTML.  # NOQA E501
            Do mind that using b64 conversion vs reading directly from filepath will be slower.  # NOQA E501
            You might need to set this to `True` in environments like Google colab.
            Defaults to False.
    """
    # this is a hack to make the code work with PIL images
    if issubclass(type(images[0]), Image.Image):
        images = np.asarray(images, dtype=type(images[0]))
    else:
        images = np.asarray(images)
    labels = np.asarray(labels) if labels is not None else labels

    if labels is None:
        labels = list(range(0, len(images)))

    html = create_imgs_grid(
        images, labels, max_images, img_width,
        zoom_scale=zoom_scale, force_b64=force_b64)

    display_html(html)


def plot_class_representations(
        images: Sequence[object],
        labels: Sequence[str or int],
        ignore_list: Sequence[str or int] = ['-1', 'unknown'],
        img_width: int = 150,
        zoom_scale: float = 2.5,
        force_b64: bool = False,
        labels_order: Sequence[str or int] = None):
    """
    Function used to display first image from each cluster/class

    Args:
        images (array):
            Array of image file paths or PIL.Image objects.
        labels (array):
            Array of labels/classes names.
        ignore_list (list, optional):
            List of classes to ignore when plotting.
            Defaults to ['-1', 'unknown'].
        img_width (int, optional):
            Width of the displayed image.
            Defaults to 150.
        zoom_scale (float, optional):
            Scale for zoom-in-on-click feature.
            Best to keep between 1.0~5.0.
            Defaults to 2.5.
        force_b64 (boolean, optional):
            You can force conversion of images to base64 instead of reading them directly from filepaths with HTML.  # NOQA E501
            Do mind that using b64 conversion vs reading directly from filepath will be slower.  # NOQA E501
            You might need to set this to `True` in environments like Google colab.
            Defaults to False.
    """
    assert(len(images) == len(labels))

    # this is a hack to make the code work with PIL images
    if issubclass(type(images[0]), Image.Image):
        images = np.asarray(images, dtype=type(images[0]))
    else:
        images = np.asarray(images)
    labels = np.asarray(labels)
    ignore_list = np.asarray(ignore_list) if ignore_list is not None else ignore_list  # NOQA E501
    labels_order = np.asarray(labels_order) if labels_order is not None else labels_order  # NOQA E501

    images, labels = get_class_representations(
        images, labels, ignore_list, labels_order)

    plot_images(
        images,
        labels=labels,
        max_images=len(images),
        img_width=img_width,
        zoom_scale=zoom_scale,
        force_b64=force_b64)

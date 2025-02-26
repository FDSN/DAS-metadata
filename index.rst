.. FDSN DAS Metadata documentation master file

Overview
========================

The `International Federation of Digital Seismograph Networks
<http://www.fdsn.org/>`_ (FDSN) defines **DAS Metadata** as a metadata
format for describing Distributed Acoustic Sensing (DAS) data sets.

The goals of this format are to provide an open standard for the description of
DAS data sets to allow compare and integrate measurements across deployments, to
make the data reusable by others following Findable, Accessible, Interoperable,
and Reusable (FAIR) data principles, to facilitate the exchange of metadata
between users and data centers, and to provide a mechanism for data centers to
validate the correctness of metadata. The format is designed to be flexible and
extensible to accommodate the wide variety of data sets that are collected by
different organizations.

This standard fully describes the five key components of a DAS experiment:
interrogator, data acquisition, channels, cable, and fiber. The intent is that
this metadata standard should be independent of the specific implementation and
the emphasis is on the content and structure (i.e., schema). This also implies
that the metadata is independent of the time-series data.

Getting started
-----------------

1. Read the :ref:`terms-and-definitions` to understand the key concepts and
   terminology used in the schema.

2. Read about the :ref:`structure` to understand the organization of the schema.

3. Review the :ref:`example-scenarios` to see how the schema can be used to
   describe different DAS deployments.

4. Review the :ref:`examples` to see how the schema can be used to describe
   specific DAS deployments.

How to contribute
-----------------

Outstanding issues and feature requests are tracked on the `GitHub issue
tracker <https://github.com/FDSN/DAS-metadata/issues>`_. If you have a question
or would like to propose a change, please open an issue.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   self
   schema
   example-scenarios
   examples
   changes
   license
   FDSN home <https://www.fdsn.org/>

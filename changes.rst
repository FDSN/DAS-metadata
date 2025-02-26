.. _changes:

Changes
========================

v.2.0 FDSN DRAFT (February 2025)
---------------------------------

**DRAFT** FDSN DAS Metadata Schema v2.0 is created based on the v1.1 DAS-RCN schema with the
following changes:

-   Add a requried schema version number
-   Add a FDSN schema identifier ($id)
-   Limit the `network_code` field to characters allowed by the FDSN Source Identifier
    specification to ensure compatibility.
-   Remove the `channel_group_id`, `interrogator_id`, `acquisition_id`, and `cable_id` fields from
    sub-structures.  They are not needed in this hierarchical structure where those values
    are unambiguous via context.
-   Remove the allowance for optional fields to be specified as `null`.  Whether a field is
    optional or required is specified using the JSON Schema features and this simplifies the
    logic for readers determining if an optional field is set.  This does not effect the
    information content of the schema, only the syntax.

v1.1.0 (September 21, 2023)
---------------------------

This updated DAS Metadata Schema introduces significant changes, including the creation of distinct
child branches for Cable (and Fiber) and for Interrogator (including Acquisition, Channel Group,
and Channel). Subsequent modifications to the GitHub repository consist of minor editorial edits
with no major structural or functional changes.

Citation:

- [journal article] Voon-Hui Lai, Kathleen M. Hodgkinson, Robert W. Porritt, Robert Mellors;
  Toward a Metadata Standard for Distributed Acoustic Sensing (DAS) Data Collection.
  Seismological Research Letters 2024;; 95 (3): 1986–1999. doi: https://doi.org/10.1785/0220230325

v1.0.0 (August 24, 2022)
-------------------------

Initial release of the DAS Metadata Reporting Format developed by the DAS Research Coordination Network Data Management Working Group.
The schema and framework were outlined in an accompanying white paper (unpublished, no DOI) and supported by two conference presentations.

References:

- [White paper] Mellors, Rob, Hodgkinson, Kathleen, Lai, Voon Hui, and
  DAS Data Management Working Group. Distributed Acoustic Sensing (DAS) Metadata Model. May 5, 2022

- [Conference paper] Mellors, Rob, Hodgkinson, Kathleen, Lai, Voon Hui, and DAS Data
  Management Working Group. Initial steps towards a DAS metadata model.
  United States: N. p., 2022. Web. doi:10.2172/2002283.

- [Conference paper] Hodgkinson, Kathleen Marian, Lai, Voon Hui, Mellors, Robert J., Porritt, Robert William,
  and Stanciu, Adrian Christian. A Metadata Exchange Model for Distributed Acoustic Sensing (DAS).
  United States: N. p., 2023. Web. doi:10.2172/2432128.

CREATE TABLE dbo.jurisdiction(
	Id					int IDENTITY(1,1),
	Name				nvarchar(255),
	SourceId			UNIQUEIDENTIFIER PRIMARY KEY

);

CREATE TABLE dbo.issuing_body(
	Id					int IDENTITY(1,1),
	Name				nvarchar(255),
	SourceId			UNIQUEIDENTIFIER PRIMARY KEY

);

CREATE TABLE dbo.legislations(
	LegislationVersionId			int NOT NULL PRIMARY KEY,
	LegislationSourceId				UNIQUEIDENTIFIER,
	LegislationVersionOrdinal		int,
	Title							nvarchar(max),
	NativeTitle						nvarchar(max),
	IssuingBodySourceId				UNIQUEIDENTIFIER,
	JurisdictionSourceId			UNIQUEIDENTIFIER

	FOREIGN KEY (IssuingBodySourceId) REFERENCES dbo.issuing_body (SourceId),
	FOREIGN KEY (JurisdictionSourceId) REFERENCES dbo.jurisdiction (SourceId)
);


CREATE TABLE dbo.part(
	PartVersionId					int,
	LegislationVersionId			int,
	PartSourceId					UNIQUEIDENTIFIER NOT NULL,
	PartVersionOrdinal				int NOT NULL,
	OrderNum						int,
	Content							nvarchar(max),
	NativeContent					nvarchar(max),
	ParentPartVersionId				int


	FOREIGN KEY (LegislationVersionId) REFERENCES dbo.legislations(LegislationVersionId)
);

ALTER TABLE dbo.part
    ADD CONSTRAINT pk_legislationConstraint PRIMARY KEY (PartSourceId, PartVersionOrdinal)
GO
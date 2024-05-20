create table [Marche]
(
    [Num_Contrat]       varchar(500)        not null
        constraint Marche_pk
            primary key,
    [Num_Avenant]       int       default 0 not null,
    [Code_site]         varchar(10)         not null,
    [NT]                varchar(20)         not null,
    [libelle]           varchar(max)        not null,
    [ods_depart]        date                not null,
    [delais]            int,
    [revisable]         bit       default 0,
    [delai_paiement_f]  int       default 0,
    [rabais]            float     default 0,
    [tva]               float     default 0,
    [rg]                float     default 0,
    [date_signature]    date                not null,
	[Est_Bloquer]       bit          not null,
    [User_ID]           varchar(15),
    [Date_Modification] datetime2 default getdate(),
)
go

create index [Marche_Code_Site_index]
    on [Marche] ([Code_site])
go

create index [Marche_NT_index]
    on [Marche] ([NT])
go

create index [Marche_Num_Avenant_index]
    on [Marche] ([Num_Avenant])
go

ALTER TABLE [Marche] ADD CONSTRAINT FK_Code_Site_NT_Code_Tache_Marche FOREIGN KEY  ([Code_Site],[NT]) REFERENCES [Tab_NT] ([Code_Site],[NT]);

/******************************************************************/

create table [Marche_Avenant]
(
    [Num_Contrat]       varchar(500)        not null,
    [Num_Avenant]       int       default 0 not null,
    [Code_site]         varchar(10)         not null,
    [NT]                varchar(20)         not null,
    [libelle]           varchar(max)        not null,
    [ods_depart]        date                not null,
    [delais]            int,
    [revisable]         bit       default 0,
    [delai_paiement_f]  int       default 0,
    [rabais]            float     default 0,
    [tva]               float     default 0,
    [rg]                float     default 0,
    [date_signature]    date                not null,
	[Est_Bloquer]       bit          not null,
    [User_ID]           varchar(15),
    [Date_Modification] datetime2 default getdate(),
    
)
go

create index [Marche_Avenant_Code_Site_index]
    on [Marche_Avenant] ([Code_site])
go

create index [Marche_Avenant_NT_index]
    on [Marche_Avenant] ([NT])
go

create index [Marche_Avenant_Num_Avenant_index]
    on [Marche_Avenant] ([Num_Avenant])
go

create index [Marche_Avenant_Num_Contrat_index]
    on [Marche_Avenant] ([Num_Contrat])
go


ALTER TABLE [Marche_Avenant] ADD CONSTRAINT Marche_Avenant_PK PRIMARY KEY  ([Num_Contrat],[Num_Avenant]) 
ALTER TABLE [Marche_Avenant] ADD CONSTRAINT FK_Code_Site_NT_Code_Tache_Marche_Avenant FOREIGN KEY  ([Code_Site],[NT]) REFERENCES [Tab_NT] ([Code_Site],[NT]);

/******************************************************************/
create table [Mode_Paiement]
(
    [Id_Mode]           int identity
        constraint PK__Mode_Paiement__id
            primary key,

    [libelle]           varchar(500) not null,
    [Est_Bloquer]       bit          not null,
    [User_ID]           varchar(15)  not null,
    [Date_Modification] datetime2 default getdate()
)
go
create index [Mode_Paiement_Id_Mode_index]
    on [Mode_Paiement] ([Id_Mode])
go


/******************************************************************/

create table [Type_Avance]
(
    [Id_Type_Avance]    int identity
        constraint PK__TypeAvance_Id_Type_Avance
            primary key,
    [Libelle]           varchar(500) not null,
    [Taux]              float        not null,
	[Est_Bloquer]       bit          not null,
    [User_ID]           varchar(15),
    [Date_Modification] datetime2 default getdate()
)
go

create index [Type_Avance_Id_Type_Avance_index]
    on [Type_Avance]([Id_Type_Avance])
go

/******************************************************************/

create table [Type_Caution]
(
    [Id_Type_Caution]   int identity
        constraint PK__Type_Caution_Id_Type_Caution
            primary key,
    [libelle]           varchar(500),
    [Taux_Exact]        float,
    [Taux_Min]          float,
    [Taux_Max]          float,
    [Type_Avance]       int,
	[Est_Bloquer]       bit          not null,
    [User_ID]           varchar(15),
    [Date_Modification] datetime2 default getdate()
)
go

create index [Type_Caution_Id_Type_Caution_index]
    on [Type_Caution]([Id_Type_Caution])
go

ALTER TABLE [Type_Caution] ADD CONSTRAINT FK_Type_Avance_Type_Caution FOREIGN KEY  ([Type_Avance]) REFERENCES [Type_Avance] ([Id_Type_Avance]);

/******************************************************************/

create table [Avances]
(
    [Id_Avance]         int identity
        constraint PK__Avances__Id_avance
            primary key,
    [num_avance]        int                  not null,
    [taux_avance]       float     default 0  not null,
    [montant]           float     default 0  not null,
    [debut]             float     default 0  not null,
    [fin]               float     default 80 not null,
    [date]              date                 not null,
    [remboursee]        bit       default 0  not null,
    [Num_Marche ]     varchar(500)         not null,
    [Type_Avance]       int                  not null,
	[Est_Bloquer]       bit          not null,
    [User_ID]           varchar(15),
    [Date_Modification] datetime2 default getdate()
)
go

create index [Avances_Type_Avance_index]
    on [Avances] ([Type_Avance])
go


ALTER TABLE [Avances] ADD CONSTRAINT FK_Num_Marche_Avances FOREIGN KEY  ([Num_Marche]) REFERENCES [Marche] ([Num_Contrat] );

ALTER TABLE [Avances] ADD CONSTRAINT FK_Type_Avance_Avances FOREIGN KEY  ([Type_Avance]) REFERENCES [Type_Avance] ([Id_Type_Avance]);


/******************************************************************/

create table [Cautions]
(
    [Id_Caution]        int identity
        constraint Cautions_pk
            primary key,
    [date_soumission]   date        not null,
    [montant]           float       not null,
    [Est_Recupere]      bit         not null,
    [Agence]            varchar(15) not null
        constraint Cautions_Tab_Agence_Code_Agence_fk
            references Tab_Agence,
    [Avance]            int,
    [Num_Marche]        varchar(500),
    [Type_Caution]      int         not null,
	[Est_Bloquer]       bit          not null,
    [User_ID]           varchar(15),
    [Date_Modification] datetime2 default getdate()
)
go

create index [Cautions_Num_Marche_id_index]
    on [Cautions] ([Num_Marche])
go

create index [Cautions_Type_Caution_index]
    on [Cautions] ([Type_Caution])
go

create index [Cautions_Avance_index]
    on [Cautions] ([Avance])
go


ALTER TABLE [Cautions] ADD CONSTRAINT FK_Num_Marche_Cautions FOREIGN KEY  ([Num_Marche]) REFERENCES [Marche] ([Num_Contrat] );

ALTER TABLE [Cautions] ADD CONSTRAINT FK_Type_Caution_Cautions FOREIGN KEY  ([Type_Caution]) REFERENCES [Type_Caution] ([Id_Type_Caution]);

ALTER TABLE [Cautions] ADD CONSTRAINT FK_Avance_Cautions FOREIGN KEY  ([Avance]) REFERENCES [Avances] ([Id_Avance]);
ALTER TABLE [Cautions] ADD CONSTRAINT FK_Agence_Cautions FOREIGN KEY  ([Agence]) REFERENCES [Tab_Agence] ([Code_Agence]);


/******************************************************************/



create table [Tab_NT_Taches_Avenant]
(
    [Code_site]                varchar(10) not null,
    [NT]                     varchar(20) not null,
    [Code_Tache]               varchar(30) not null,
    [Num_Avenant]              int          default 0 not null,
    [Est_Tache_Composite]      bit          default 0,
    [Est_Tache_Complementaire] bit          default 0,
    [Libelle_Tache]            varchar(max) default NULL,
    [Code_Unite_Mesure]        varchar(4)   default NULL,
    [Quantite]                 real         default 0,
    [Prix_Unitaire]            money        default 0,
    [Est_Bloquer]              bit          default 0,
    [User_ID]                  varchar(15)  default NULL,
    [Date_Modification]        datetime2    default getdate(),
    
)
go

create index [Tab_NT_Taches_Avenant_Code_site_index]
    on [Tab_NT_Taches_Avenant] ([Code_site])
go

create index [Tab_NT_Taches_Avenant_NT_index]
    on [Tab_NT_Taches_Avenant] ([NT])
go

create index [Tab_NT_Taches_Avenant_Code_Tache_index]
    on [Tab_NT_Taches_Avenant] ([Code_Tache])
go

create index [Tab_NT_Taches_Avenant_Num_Avenant_index]
    on [Tab_NT_Taches_Avenant] ([Num_Avenant])
go


ALTER TABLE [Tab_NT_Taches_Avenant] ADD CONSTRAINT Tab_NT_Taches_Avenant_PK PRIMARY KEY  ([Code_site], [NT], [Code_Tache],[Num_Avenant] ) 
ALTER TABLE [Tab_NT_Taches_Avenant] ADD CONSTRAINT FK_Code_Site_NT_Tab_NT_Taches_Avenant FOREIGN KEY  ([Code_Site],[NT]) REFERENCES [Tab_NT] ([Code_Site],[NT]);
ALTER TABLE [Tab_NT_Taches_Avenant] ADD CONSTRAINT FK_Code_Unite_Mesure_Tab_NT_Taches_Avenant FOREIGN KEY  ([Code_Unite_Mesure]) REFERENCES [Tab_Unite_de_Mesure] ([Code_Unite_Mesure]);





/******************************************************************/


create table [Factures]
(
    [Num_facture]       varchar(800) not null
        constraint PK__Factures__Num_Facture
            primary key,
    [Num_Situation]     int          not null,
    [Date_Debut]        date         not null,
    [Date_Fin]         date         not null,
    [date_facture]      date         not null,
    [Montant_Mois]      float     default 0,
    [Montant_RB]        float     default 0,
    [Montant_RG]        float     default 0,
    [Paye]              bit       default 0,
    [Num_Marche]        varchar(500) not null,
	[Est_Bloquer]       bit          not null,
    [User_ID]           varchar(15)  not null,
    [Date_Modification] datetime2 default getdate(),
   
)
go

create index [Factures_Num_Facture_index]
    on [Factures] ([Num_facture])
go

create index [Factures_Num_Situation_index]
    on [Factures] ([Num_Situation])
go



ALTER TABLE [Factures] ADD CONSTRAINT FK_Num_Marche_Facturess FOREIGN KEY  ([Num_Marche]) REFERENCES [Marche] ([Num_Contrat] );




/******************************************************************/



create table [Attachements]
(
    [Id_Attachement]    int identity
        constraint Attachements_pk
            primary key,
    [Num_Marche]        varchar(500),
    [Code_Site]         varchar(10) not null,
    [NT]                varchar(20) not null,
    [Code_Tache]        varchar(30) not null,
    [qte]               float     default 0,
    [prix_u]            float     default 0,
    [montant]           float     default 0,
    [Mmaa]              date        not null,
	[Est_Bloquer]       bit  default 0  not null,
    [User_ID]           varchar(15),
    [Date_Modification] datetime2 default getdate(),
	
)
go

create index [Attachements_Code_Site_index]
    on [Attachements] ([Code_Site])
go

create index [Attachements_NT_index]
    on [Attachements] ([NT])
go

create index [Attachements_Code_Tache_index]
    on [Attachements] ([Code_Tache])
go

create index [Attachements_Num_Marche_index]
    on [Attachements] ([Num_Marche])
go

create index [Attachements_Mmaa_index]
    on [Attachements] ([Mmaa])
go

ALTER TABLE [Attachements] ADD CONSTRAINT FK_Code_Site_NT_Code_Tache_Table_Attachements FOREIGN KEY  ([Code_Site],[NT],[Code_Tache]) REFERENCES [Tab_NT_Taches] ([Code_Site],[NT],[Code_Tache]);

ALTER TABLE [Attachements] ADD CONSTRAINT FK_Num_Marche_Attachements FOREIGN KEY  ([Num_Marche]) REFERENCES [Marche] ([Num_Contrat] );


/**********************************************/


create table [Detail_Facture]
(
    [id]                int identity
        constraint PK__Detail_F_id
            primary key,
			
	 [Num_Facture]       varchar(800),
    [Detail]            int       not null,
			
   
	[Est_Bloquer]       bit  default 0  not null,
	[User_ID]           varchar(15) ,
    [Date_Modification] datetime2  DEFAULT CURRENT_TIMESTAMP   ,

)
go

create index [Detail_Facture_facture_id_index]
    on [Detail_Facture] ([Num_Facture])
go
create index [Detail_Facture_Detail_index]
    on [Detail_Facture] ([Detail])
go

ALTER TABLE [Detail_Facture] ADD CONSTRAINT FK_Num_Facture_Detail_facture FOREIGN KEY  ([Num_Facture]) REFERENCES [Factures] ([Num_facture] );
ALTER TABLE [Detail_Facture] ADD CONSTRAINT FK_Detail_Detail_facture FOREIGN KEY  ([Detail]) REFERENCES [Attachements] ([Id_Attachement] );



/************************************************/


create table [Remboursement]
(
    [id]                int identity
        constraint PK__Remboursement__id
            primary key,
    [Montant]           float     default 0 not null,
    [Avance]            int,
    [Num_Facture]       varchar(800),
	[Est_Bloquer]       bit  default 0  not null,
    [User_ID]           varchar(15),
    [Date_Modification] datetime2 default getdate()
)
go

create index [Rembourcement_Num_Facture_index]
    on [Remboursement] ([Num_Facture])
go

create index [Rembourcement_Avance_id_index]
    on [Remboursement] ([Avance])
go

ALTER TABLE [Remboursement] ADD CONSTRAINT FK_Num_Facture_Remboursement FOREIGN KEY  ([Num_Facture]) REFERENCES [Factures] ([Num_facture] );

ALTER TABLE [Remboursement] ADD CONSTRAINT FK_Avance_Remboursement FOREIGN KEY  ([Avance]) REFERENCES [Avances] ([Id_Avance]);

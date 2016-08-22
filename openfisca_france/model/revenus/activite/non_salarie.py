# -*- coding: utf-8 -*-

from openfisca_france.model.base import *  # noqa


# TODO: 5QL


# Nomenclature :
# première lettre :
#    e : auto-entrepreneur
#    m : micro entreprise, déclaratif spécial
#    n : bénéfice réel sans CGA
#    a : bénéfice réel avec CGA ou viseur
#    f : forfait
#    c : déclaration contrôlée)
# trois lettres suivantes, catégorie du revenu :
#    rag : agricole
#    bic : industriel et commercial pro
#    bnc : non commercial pro
#    acc : industriel et commercial non pro
#    ncn : non commercial non pro
# après l'underscore : abbréviation du label de la case

class f5qm(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QM", u"5RM"],
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Agents généraux d’assurances: indemnités de cessation d’activité"

  # (f5qm, f5rm )

# Revenus des professions non salariées
class ppe_du_ns(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NV", u"5OV"],
        PERSONNE_A_CHARGE: u"5PV",
        }
    column = IntCol
    entity_class = Individus
    label = u"Prime pour l'emploi des non-salariés: nombre de jours travaillés dans l'année"
    stop_date = date(2006, 12, 31)

  # (f5nv, f5ov, f5pv)

class ppe_tp_ns(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NW", u"5OW"],
        PERSONNE_A_CHARGE: u"5PW",
        }
    column = BoolCol
    entity_class = Individus
    label = u"Prime pour l'emploi des non-salariés: indicateur de travail à temps plein sur l'année entière"
    stop_date = date(2006, 12, 31)

  # (f5nw, f5ow, f5pw)

class frag_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HN", u"5IN"],
        PERSONNE_A_CHARGE: u"5JN",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus agricoles exonérés (régime du forfait)"
    start_date = date(2007, 1, 1)

  # (f5hn, f5in, f5jn))

class frag_impo(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HO", u"5IO"],
        PERSONNE_A_CHARGE: u"5JO",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus agricoles imposables (régime du forfait)"
    start_date = date(2007, 1, 1)

  # (f5ho, f5io, f5jo))

class arag_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HB", u"5IB"],
        PERSONNE_A_CHARGE: u"5JB",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus agricoles exonérés yc plus-values (Régime du bénéfice réel, revenus bénéficiant de l'abattement CGA ou viseur), activités exercées en Corse"
    start_date = date(2007, 1, 1)

  # (f5hb, f5ib, f5jb))

class arag_impg(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HC", u"5IC"],
        PERSONNE_A_CHARGE: u"5JC",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus agricoles imposables, cas général moyenne triennale (Régime du bénéfice réel, revenus bénéficiant de l'abattement CGA ou viseur)"
    start_date = date(2007, 1, 1)

  # (f5hc, f5ic, f5jc))

class arag_defi(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HF", u"5IF"],
        PERSONNE_A_CHARGE: u"5JF",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits agricoles (Régime du bénéfice réel, revenus bénéficiant de l'abattement CGA ou viseur)"
    start_date = date(2007, 1, 1)

  # (f5hf, f5if, f5jf))

class nrag_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HH", u"5IH"],
        PERSONNE_A_CHARGE: u"5JH",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus agricoles exonérés yc plus-values (Régime du bénéfice réel, revenus ne bénéficiant pas de l'abattement CGA ou viseur), activités exercées en Corse"
    start_date = date(2007, 1, 1)

  # (f5hh, f5ih, f5jh))

class nrag_impg(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HI", u"5II"],
        PERSONNE_A_CHARGE: u"5JI",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus agricoles imposables, cas général moyenne triennale (Régime du bénéfice réel, revenus ne bénéficiant pas de l'abattement CGA ou viseur)"
    start_date = date(2007, 1, 1)

  # (f5hi, f5ii, f5ji))

class nrag_defi(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HL", u"5IL"],
        PERSONNE_A_CHARGE: u"5JL",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits agricoles (Régime du bénéfice réel, revenus ne bénéficiant pas de l'abattement CGA ou viseur)"
    start_date = date(2007, 1, 1)

  # (f5hl, f5il, f5jl))

class nrag_ajag(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HM", u"5IM"],
        PERSONNE_A_CHARGE: u"5JM",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Jeunes agriculteurs, Abattement de 50% ou 100% (Régime du bénéfice réel, revenus bénéficiant de l'abattement CGA ou viseur)"
    start_date = date(2007, 1, 1)

  # (f5hm, f5im, f5jm))

# Autoentrepreneur
class ebic_impv(Variable):
    cerfa_field = {
        DECLARANT: [ u"5TA", u"5UA"],
        PERSONNE_A_CHARGE: u"5VA",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux professionnels imposables: vente de marchandises et assimilées (régime auto-entrepreneur)"
    start_date = date(2009, 1, 1)
    stop_date = date(2009, 12, 31)

  # (f5ta, f5ua, f5va))

class ebic_imps(Variable):
    cerfa_field = {
        DECLARANT: [ u"5TB", u"5UB"],
        PERSONNE_A_CHARGE: u"5VB",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux professionnels imposables: prestations de services et locations meublées (régime auto-entrepreneur)"
    start_date = date(2009, 1, 1)
    stop_date = date(2009, 12, 31)

  # (f5tb, f5ub, f5vb))

class ebnc_impo(Variable):
    cerfa_field = {
        DECLARANT: [ u"5TE", u"5UE"],
        PERSONNE_A_CHARGE: u"5VE",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus non commerciaux (régime auto-entrepreneur ayant opté pour le versement libératoire)"
    start_date = date(2009, 1, 1)
    stop_date = date(2009, 12, 31)

  # (f5te, f5ue, f5ve))

class mbic_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KN", u"5LN"],
        PERSONNE_A_CHARGE: u"5MN",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux professionnels nets exonérés (régime micro entreprise)"

  # (f5kn, f5ln, f5mn))

class abic_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KB", u"5LB"],
        PERSONNE_A_CHARGE: u"5MB",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux nets exonérés yc plus-values avec CGA ou viseur (régime du bénéfice réel)"

  # (f5kb, f5lb, f5mb))

class nbic_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KH", u"5LH"],
        PERSONNE_A_CHARGE: u"5MH",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux nets exonérés yc plus-values sans CGA (régime du bénéfice réel)"

  # (f5kh, f5lh, f5mh))

class mbic_impv(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KO", u"5LO"],
        PERSONNE_A_CHARGE: u"5MO",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux professionnels imposables: vente de marchandises (régime micro entreprise)"

  # (f5ko, f5lo, f5mo))

class mbic_imps(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KP", u"5LP"],
        PERSONNE_A_CHARGE: u"5MP",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux professionnels imposables: prestations de services et locations meublées (régime micro entreprise)"

  # (f5kp, f5lp, f5mp))

class abic_impn(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KC", u"5LC"],
        PERSONNE_A_CHARGE: u"5MC",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux imposables: régime normal ou simplifié avec CGA ou viseur (régime du bénéfice réel)"

  # (f5kc, f5lc, f5mc))

class abic_imps(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KD", u"5LD"],
        PERSONNE_A_CHARGE: u"5MD",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux imposables: régime simplifié avec CGA ou viseur (régime du bénéfice réel)"
    stop_date = date(2009, 12, 31)

  # (f5kd, f5ld, f5md))


class nbic_impn(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KI", u"5LI"],
        PERSONNE_A_CHARGE: u"5MI",
        }

    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux professionnels imposables: régime normal ou simplifié sans CGA (régime du bénéfice réel)"

  # (f5ki, f5li, f5mi))

# """
# réutilisation cases 2013
# """
class nbic_imps(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KJ", u"5LJ"],
        PERSONNE_A_CHARGE: u"5MJ",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux professionnels imposables: régime simplifié sans CGA (régime du bénéfice réel)"
    stop_date = date(2009, 12, 31)

 # TODO: c'est 5HU pour les années anciennes

class nbic_mvct(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KJ", u"5LJ"],
        PERSONNE_A_CHARGE: u"5MJ",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux professionnels moins-values nettes à court terme"
    start_date = date(2012, 1, 1)

  # (f5kj, f5lj, f5mj))
                                                          # vérifier date début #####à intégrer dans OF#######

class abic_defn(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KF", u"5LF"],
        PERSONNE_A_CHARGE: u"5MF",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits industriels et commerciaux: régime normal ou simplifié avec CGA ou viseur (régime du bénéfice réel)"

  # (f5kf, f5lf, f5mf))

class abic_defs(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KG", u"5LG"],
        PERSONNE_A_CHARGE: u"5MG",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits industriels et commerciaux: simplifié avec CGA ou viseur (régime du bénéfice réel)"
    stop_date = date(2009, 12, 1)

  # (f5kg, f5lg, f5mg))
                                                          # vérif <=2012

class nbic_defn(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KL", u"5LL"],
        PERSONNE_A_CHARGE: u"5ML",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits industriels et commerciaux: régime normal ou simplifié sans CGA (régime du bénéfice réel)"

  # (f5kl, f5ll, f5ml))

class nbic_defs(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KM", u"5LM"],
        PERSONNE_A_CHARGE: u"5MM",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Locations déjà soumises aux prélèvements sociaux sans CGA (régime du bénéfice réel)"
    stop_date = date(2009, 12, 31)

  # (f5km, f5lm, f5mm))

class nbic_apch(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KS", u"5LS"],
        PERSONNE_A_CHARGE: u"5MS",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Artisans pêcheurs : abattement 50% avec CGA ou viseur (régime du bénéfice réel)"

  # (f5ks, f5ls, f5ms))

class macc_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NN", u"5ON"],
        PERSONNE_A_CHARGE: u"5PN",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux non professionnels nets exonérés (régime micro entreprise)"

  # (f5nn, f5on, f5pn))

class aacc_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NB", u"5OB"],
        PERSONNE_A_CHARGE: u"5PB",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux non professionnels exonérés yc plus-values avec CGA ou viseur (régime du bénéfice réel)"

  # (f5nb, f5ob, f5pb))

class nacc_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NH", u"5OH"],
        PERSONNE_A_CHARGE: u"5PH",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux non professionnels exonérés yc plus-values sans CGA (régime du bénéfice réel)"

  # (f5nh, f5oh, f5ph))

class macc_impv(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NO", u"5OO"],
        PERSONNE_A_CHARGE: u"5PO",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux non professionnels imposables: vente de marchandises et assimilées (régime micro entreprise)"

  # (f5no, f5oo, f5po))

class macc_imps(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NP", u"5OP"],
        PERSONNE_A_CHARGE: u"5PP",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux non professionnels imposables: prestations de services (régime micro entreprise)"

  # (f5np, f5op, f5pp))

class aacc_impn(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NC", u"5OC"],
        PERSONNE_A_CHARGE: u"5PC",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux non professionnels imposables: régime normal ou simplifié avec CGA ou viseur (régime du bénéfice réel)"

  # (f5nc, f5oc, f5pc))

class aacc_imps(Variable):
    cerfa_field = {
        DECLARANT: [ u"5ND", u"5OD"],
        PERSONNE_A_CHARGE: u"5PD",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Locations meublées non professionnelles (régime micro entreprise)"
    start_date = date(2011, 1, 1)

  # (f5nd, f5od, f5pd)) #TODO: avant 2010

class aacc_defn(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NF", u"5OF"],
        PERSONNE_A_CHARGE: u"5PF",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits industriels et commerciaux non professionnels: régime normal ou simplifié avec CGA ou viseur (régime du bénéfice réel)"

  # (f5nf, f5of, f5pf))

class aacc_gits(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NG", u"5OG"],
        PERSONNE_A_CHARGE: u"5PG",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Location de gîtes ruraux, chambres d'hôtes et meublés de tourisme (régime micro entreprise)"
    start_date = date(2011, 1, 1)

  # (f5ng, f5og, f5pg))

class nacc_impn(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NI", u"5OI"],
        PERSONNE_A_CHARGE: u"5PI",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus industriels et commerciaux non professionnels imposables: régime normal ou simplifié sans CGA (régime du bénéfice réel)"

  # (f5ni, f5oi, f5pi))

class aacc_defs(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NG", u"5OG"],
        PERSONNE_A_CHARGE: u"5PG",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits de revenus industriels et commerciaux non professionnels avec CGA (régime simplifié du bénéfice réel)"
    stop_date = date(2009, 12, 31)



class nacc_meup(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NJ", u"5OJ"],
        PERSONNE_A_CHARGE: u"5PJ",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Locations meublées non professionnelles: Locations déjà soumises aux prélèvements sociaux (régime micro entreprise)"
    start_date = date(2012, 1, 1)

  # (f5nj, f5oj, f5pj)) #TODO: dates 5PJ, 5PG, 5PD, 5OM

class nacc_defn(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NL", u"5OL"],
        PERSONNE_A_CHARGE: u"5PL",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits industriels et commerciaux non professionnels: régime normal ou simplifié sans CGA (régime du bénéfice réel)"

  # (f5nl, f5ol, f5pl))

class nacc_defs(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NM", u"5OM"],
        PERSONNE_A_CHARGE: u"5PM",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Locations meublées non professionnelles: Gîtes ruraux et chambres d'hôtes déjà soumis aux prélèvements sociaux avec CGA (régime du bénéfice réel)"
    start_date = date(2012, 1, 1)

  # (f5nm, f5om, f5pm)) #TODO autres 5NM

class mncn_impo(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KU", u"5LU"],
        PERSONNE_A_CHARGE: u"5MU",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus non commerciaux non professionnels imposables (régime déclaratif spécial ou micro BNC)"

  # (f5ku, f5lu, f5mu))

class cncn_bene(Variable):
    cerfa_field = {
        DECLARANT: [ u"5SN", u"5NS"],
        PERSONNE_A_CHARGE: u"5OS",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus non commerciaux non professionnels imposables sans AA (régime de la déclaration controlée)"
    start_date = date(2006, 1, 1)

  # (f5sn, f5ns, f5os))

class cncn_defi(Variable):
    cerfa_field = {
        DECLARANT: [ u"5SP", u"5NU"],
        PERSONNE_A_CHARGE: u"5OU",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits non commerciaux non professionnels sans AA (régime de la déclaration controlée)"
    start_date = date(2006, 1, 1)

  # (f5sp, f5nu, f5ou, f5sr))
                                                                  # pas de f5sr en 2013

class mbnc_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HP", u"5IP"],
        PERSONNE_A_CHARGE: u"5JP",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus non commerciaux professionnels nets exonérés (régime déclaratif spécial ou micro BNC)"

  # (f5hp, f5ip, f5jp))

class abnc_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QB", u"5RB"],
        PERSONNE_A_CHARGE: u"5SB",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus non commerciaux professionnels exonérés (yc compris plus-values) (régime de la déclaration controlée, revenus bénéficiant de l'abattement association agrée ou viseur)"

  # (f5qb, f5rb, f5sb))

class nbnc_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QH", u"5RH"],
        PERSONNE_A_CHARGE: u"5SH",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus non commerciaux professionnels exonérés (yc compris plus-values) (régime de la déclaration controlée, revenus ne bénéficiant pas de l'abattement association agrée)"

  # (f5qh, f5rh, f5sh))

class mbnc_impo(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HQ", u"5IQ"],
        PERSONNE_A_CHARGE: u"5JQ",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus non commerciaux professionnels imposables (régime déclaratif spécial ou micro BNC)"

  # (f5hq, f5iq, f5jq))

class abnc_impo(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QC", u"5RC"],
        PERSONNE_A_CHARGE: u"5SC",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus non commerciaux professionnels imposables (régime de la déclaration controlée, revenus bénéficiant de l'abattement association agrée ou viseur)"

  # (f5qc, f5rc, f5sc))

class abnc_defi(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QE", u"5RE"],
        PERSONNE_A_CHARGE: u"5SE",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits non commerciaux professionnels (régime de la déclaration controlée, revenus bénéficiant de l'abattement association agrée ou viseur)"

  # (f5qe, f5re, f5se))

class nbnc_impo(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QI", u"5RI"],
        PERSONNE_A_CHARGE: u"5SI",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus non commerciaux professionnels imposables (régime de la déclaration controlée, revenus ne bénéficiant pas de l'abattement association agrée)"

  # (f5qi, f5ri, f5si))

class nbnc_defi(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QK", u"5RK"],
        PERSONNE_A_CHARGE: u"5SK",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits non commerciaux professionnels (régime de la déclaration controlée, revenus ne bénéficiant pas de l'abattement association agrée)"

  # (f5qk, f5rk, f5sk))

class mbic_mvct(Variable):
    cerfa_field = u"5HU"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Moins-values industrielles et commerciales nettes à court terme du foyer (régime micro entreprise)"
    stop_date = date(2011, 12, 31)

  # (f5hu))
                                                          # vérif <=2012

class macc_mvct(Variable):
    cerfa_field = u"5IU"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Moins-values industrielles et commerciales non professionnelles nettes à court terme du foyer (régime micro entreprise)"

  # (f5iu))

class mncn_mvct(Variable):
    cerfa_field = u"JU"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Moins-values non commerciales non professionnelles nettes à court terme du foyer (régime déclaratif spécial ou micro BNC)"

  # (f5ju))

class mbnc_mvct(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KZ", u"5LZ"], #TODO: pb cerfa field
        PERSONNE_A_CHARGE: u"5MZ",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Moins-values non commerciales professionnelles nettes à court terme (régime déclaratif spécial ou micro BNC)"
    start_date = date(2012, 1, 1)

  # (f5kz, f5lz , f5mz), f5lz , f5mz sont présentent en 2013


class frag_pvct(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HW", u"5IW"],
        PERSONNE_A_CHARGE: u"5JW",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values agricoles  à court terme (régime du forfait)"
    start_date = date(2007, 1, 1)

  # (f5hw, f5iw, f5jw))

class mbic_pvct(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KX", u"5LX"],
        PERSONNE_A_CHARGE: u"5MX",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values industrielles et commerciales professionnels imposables: plus-values nettes à court terme (régime micro entreprise)"

  # (f5kx, f5lx, f5mx))

class macc_pvct(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NX", u"5OX"],
        PERSONNE_A_CHARGE: u"5PX",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values industrielles et commerciales non professionnelles imposables: plus-values nettes à court terme (régime micro entreprise)"

  # (f5nx, f5ox, f5px))

class mbnc_pvct(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HV", u"5IV"],
        PERSONNE_A_CHARGE: u"5JV",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values non commerciales professionnelles imposables et Plus-values nettes à court terme (régime déclaratif spécial ou micro BNC)"

  # (f5hv, f5iv, f5jv))

class mncn_pvct(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KY", u"5LY"],
        PERSONNE_A_CHARGE: u"5MY",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values non commerciales non professionnelles imposables et plus-values nettes à court terme (régime déclaratif spécial ou micro BNC)"

  # (f5ky, f5ly, f5my))

class mbic_mvlt(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KR", u"5LR"],
        PERSONNE_A_CHARGE: u"5MR",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Moins-values industrielles et commerciales professionnels à long terme (régime micro entreprise)"

  # (f5kr, f5lr, f5mr))

class macc_mvlt(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NR", u"5OR"],
        PERSONNE_A_CHARGE: u"5PR",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Moins-values industrielles et commerciales non professionnelles à long terme (régime micro entreprise)"

  # (f5nr, f5or, f5pr))

class mncn_mvlt(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KW", u"5LW"],
        PERSONNE_A_CHARGE: u"5MW",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Moins-values non commerciales non professionnelles à long terme (régime déclaratif spécial ou micro BNC)"

  # (f5kw, f5lw, f5mw))

class mbnc_mvlt(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HS", u"5IS"],
        PERSONNE_A_CHARGE: u"5JS",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Moins-values non commerciales professionnelles à long terme (régime déclaratif spécial ou micro BNC)"

  # (f5hs, f5is, f5js))

class frag_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HX", u"5IX"],
        PERSONNE_A_CHARGE: u"5JX",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values agricoles de cession taxables à 16% (régime du forfait)"
    start_date = date(2007, 1, 1)

  # (f5hx, f5ix, f5jx))

class arag_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HE", u"5IE"],
        PERSONNE_A_CHARGE: u"5JE",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values agricoles de cession taxables à 16% (Régime du bénéfice réel, revenus bénéficiant de l'abattement CGA ou viseur)"
    start_date = date(2007, 1, 1)

  # (f5he, f5ie, f5je))

class nrag_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HK", u"5LK"],
        PERSONNE_A_CHARGE: u"5JK",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values agricoles de cession taxables à 16% (Régime du bénéfice réel, revenus ne bénéficiant pas de l'abattement CGA ou viseur)"
    stop_date = date(2006, 12, 31)

  # TODO: vérif <=2012))  # (f5hk, f5lk, f5jk) codent autre chose sur d'autres années),

class mbic_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KQ", u"5LQ"],
        PERSONNE_A_CHARGE: u"5MQ",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values industrielles et commerciales professionnelles imposables: plus-values de cession taxables à 16% (régime micro entreprise)"

  # (f5kq, f5lq, f5mq))

class abic_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KE", u"5LE"],
        PERSONNE_A_CHARGE: u"5ME",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values industrielles et commerciales de cession taxables à 16% avec CGA ou viseur (régime du bénéfice réel)"

  # (f5ke, f5le, f5me))

class nbic_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5IK", u"5KK"],
        PERSONNE_A_CHARGE: u"5MK",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus non commerciaux non professionnels exonérés sans AA (régime de la déclaration controlée)"
    start_date = date(2008, 1, 1)

  # (f5kk, f5ik, f5mk)) TODO: autre 5KK 2005/20006

class macc_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NQ", u"5OQ"],
        PERSONNE_A_CHARGE: u"5PQ",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values industrielles et commerciales non professionnelles imposables: plus-values de cession taxables à 16% (régime micro entreprise)"

  # (f5nq, f5oq, f5pq))

class aacc_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NE", u"5OE"],
        PERSONNE_A_CHARGE: u"5PE",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values industrielles et commerciales non professionnelles de cession taxables à 16% avec CGA ou viseur (régime du bénéfice réel)"

  # (f5ne, f5oe, f5pe))

class nacc_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NK", u"5OK"],
        PERSONNE_A_CHARGE: u"5PK",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Locations meublées non professionnelles: Revenus imposables sans CGA (régime du bénéfice réel)"
    start_date = date(2009, 1, 1)
    stop_date = date(2010, 12, 31)

  # (f5nk, f5ok, f5pk)) TODO: 5NK 2005/2006

class mncn_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KV", u"5LV"],
        PERSONNE_A_CHARGE: u"5MV",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values non commerciales non professionnelles de cession taxables à 16% (régime déclaratif spécial ou micro BNC)"

  # (f5kv, f5lv, f5mv))

class cncn_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5SO", u"5NT"],
        PERSONNE_A_CHARGE: u"5OT",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values non commerciales non professionnelles taxables à 16% avec AA ou viseur (régime de la déclaration controlée)"
    start_date = date(2006, 1, 1)

  # (f5so, f5nt, f5ot))

class mbnc_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HR", u"5IR"],
        PERSONNE_A_CHARGE: u"5JR",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values non commerciales professionnelles de cession taxables à 16% (régime déclaratif spécial ou micro BNC)"

  # (f5hr, f5ir, f5jr))

class abnc_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QD", u"5RD"],
        PERSONNE_A_CHARGE: u"5SD",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Plus-values non commerciaux professionnels de cession taxables à 16% (régime de la déclaration controlée, revenus bénéficiant de l'abattement association agrée ou viseur)"

  # (f5qd, f5rd, f5sd))

class nbnc_pvce(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QJ", u"5RJ"],
        PERSONNE_A_CHARGE: u"5SJ",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits industriels et commerciaux: locations meublées sans CGA (régime du bénéfice réel)"
    start_date = date(2009, 1, 1)

  # (f5qj, f5rj, f5sj)) #TODO 5*J 2005/2006 (qui se transforme en 5*D...)

class frag_fore(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HD", u"5ID"],
        PERSONNE_A_CHARGE: u"5JD",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus des exploitants forestiers (régime du forfait)"
    start_date = date(2007, 1, 1)



class arag_sjag(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HZ", u"5IZ"],
        PERSONNE_A_CHARGE: u"5JZ",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Abattement pour les jeunes agriculteurs des revenus agricoles sans CGA (régime du bénéfice réel)"
    start_date = date(2011, 1, 1)



class abic_impm(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HA", u"5IA"],
        PERSONNE_A_CHARGE: u"5JA",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Locations meublées imposables avec CGA ou viseur (régime du bénéfice réel pour les revenus industriels et commerciaux professionnels)"
    start_date = date(2009, 1, 1)



class nbic_impm(Variable):
    cerfa_field = {
        DECLARANT: [ u"5KA", u"5LA"],
        PERSONNE_A_CHARGE: u"5MA",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Locations meublées imposables sans CGA (régime du bénéfice réel)"
    start_date = date(2009, 1, 1)



class abic_defm(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QA", u"5RA"],
        PERSONNE_A_CHARGE: u"5SA",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits de locations meubléesavec CGA ou viseur (régime du bénéfice réel pour les revenus industriels et commerciaux professionnels)"
    start_date = date(2009, 1, 1)



class alnp_imps(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NA", u"5OA"],
        PERSONNE_A_CHARGE: u"5PA",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Locations meublées non professionnelles imposables avec CGA ou viseur (régime du bénéfice réel)"
    start_date = date(2009, 1, 1)
    stop_date = date(2010, 12, 31)



class alnp_defs(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NY", u"5OY"],
        PERSONNE_A_CHARGE: u"5PY",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits de locations meublées non professionnelles avec CGA ou viseur (régime du bénéfice réel)"
    start_date = date(2009, 1, 1)
    stop_date = date(2010, 12, 31)



class nlnp_defs(Variable):
    cerfa_field = {
        DECLARANT: [ u"5NZ", u"5OZ"],
        PERSONNE_A_CHARGE: u"5PZ",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits de locations meublées non professionnelles imposables sans CGA (régime du bénéfice réel)"
    start_date = date(2009, 1, 1)
    stop_date = date(2010, 12, 31)



class cbnc_assc(Variable):
    cerfa_field = {
        DECLARANT: [ u"5QM", u"5RM",]
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Agents généraux d'assurances : indemnités de cessation d'activité (revenus non commerciaux professionnels, régime de la déclaration contrôlée)"
    start_date = date(2006, 1, 1)



class abnc_proc(Variable):
    cerfa_field = {
        DECLARANT: [ u"5TF", u"5UF"],
        PERSONNE_A_CHARGE: u"5VF",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Honoraires de prospection commerciale exonérés avec CGA ou viseur (revenus non commerciaux professionnels, régime de la déclaration contrôlée)"
    start_date = date(2009, 1, 1)



class nbnc_proc(Variable):
    cerfa_field = {
        DECLARANT: [ u"5TI", u"5UI"],
        PERSONNE_A_CHARGE: u"5VI",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Honoraires de prospection commerciale exonérés sans CGA (revenus non commerciaux professionnels, régime de la déclaration contrôlée)"
    start_date = date(2009, 1, 1)



class mncn_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5TH", u"5UH"],
        PERSONNE_A_CHARGE: u"5VH",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus nets exonérés non commerciaux non professionnels (régime déclaratif spécial ou micro BNC)"
    start_date = date(2009, 1, 1)



class cncn_exon(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HK", u"5JK"],
        PERSONNE_A_CHARGE: u"5LK",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus nets exonérés non commerciaux non professionnels (régime de la déclaration contrôlée)"
    start_date = date(2008, 1, 1)



class cncn_aimp(Variable):
    cerfa_field = {
        DECLARANT: [ u"5JG", u"5RF"],
        PERSONNE_A_CHARGE: u"5SF",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus imposables non commerciaux non professionnels avec CGA (régime de la déclaration contrôlée)"
    start_date = date(2007, 1, 1)



class cncn_adef(Variable):
    cerfa_field = {
        DECLARANT: [ u"5JJ", u"5RG"],
        PERSONNE_A_CHARGE: u"5SG",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Déficits non commerciaux non professionnels avec CGA (régime de la déclaration contrôlée)"
    start_date = date(2007, 1, 1)



class cncn_info(Variable):
    cerfa_field = {
        DECLARANT: [ u"5TC", u"5UC"],
        PERSONNE_A_CHARGE: u"5VC",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Inventeurs et auteurs de logiciels : produits taxables à 16%, revenus non commerciaux non professionnels avec CGA (régime de la déclaration contrôlée)"
    start_date = date(2009, 1, 1)



class cncn_jcre(Variable):
    cerfa_field = {
        DECLARANT: [ u"5SV", u"5SW"],
        PERSONNE_A_CHARGE: u"5SX",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Jeunes créateurs : abattement de 50%, revenus non commerciaux non professionnels avec CGA (régime de la déclaration contrôlée)"
    start_date = date(2006, 1, 1)



class revimpres(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HY", u"5IY"],
        PERSONNE_A_CHARGE: u"5JY",
        }
    column = IntCol(val_type = "monetary")
    entity_class = Individus
    label = u"Revenus nets à imposer aux prélèvements sociaux"



class pveximpres(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HG", u"5IG"]
        }
    column = IntCol
    entity_class = Individus
    label = u"Plus-values à long terme exonérées en cas de départ à la retraite à imposer aux prélèvements sociaux"
    start_date = date(2006, 1, 1)




class pvtaimpres(Variable):
    cerfa_field = {
        DECLARANT: [ u"5HZ", u"5IZ"],
        PERSONNE_A_CHARGE: u"5JZ",
        }
    column = IntCol
    entity_class = Individus
    label = u"Plus-values à long terme taxables à 16% à la retraite à imposer aux prélèvements sociaux"
    stop_date = date(2009, 12, 31)



class f5qf(Variable):
    cerfa_field = u"5QF"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus agricoles des années antérieures non encore déduits (n-6)"
    start_date = date(2007, 1, 1)



class f5qg(Variable):
    cerfa_field = u"5QG"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus agricoles des années antérieures non encore déduits (n-5)"
    start_date = date(2007, 1, 1)



class f5qn(Variable):
    cerfa_field = u"5QN"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus agricoles des années antérieures non encore déduits (n-4)"
    start_date = date(2007, 1, 1)



class f5qo(Variable):
    cerfa_field = u"5QO"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus agricoles des années antérieures non encore déduits (n-3)"
    start_date = date(2007, 1, 1)



class f5qp(Variable):
    cerfa_field = u"5QP"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus agricoles des années antérieures non encore déduits (n-2)"
    start_date = date(2007, 1, 1)



class f5qq(Variable):
    cerfa_field = u"5QQ"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus agricoles des années antérieures non encore déduits (n-1)"
    start_date = date(2007, 1, 1)



class f5ga(Variable):
    cerfa_field = u"5GA"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus de locations meublées non professionnelles années antérieures non encore déduits (n-10)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5gb(Variable):
    cerfa_field = u"5GB"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus de locations meublées non professionnelles années antérieures non encore déduits (n-9)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5gc(Variable):
    cerfa_field = u"5GC"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus de locations meublées non professionnelles années antérieures non encore déduits (n-8)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5gd(Variable):
    cerfa_field = u"5GD"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus de locations meublées non professionnelles années antérieures non encore déduits (n-7)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5ge(Variable):
    cerfa_field = u"5GE"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus de locations meublées non professionnelles années antérieures non encore déduits (n-6)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5gf(Variable):
    cerfa_field = u"5GF"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus de locations meublées non professionnelles années antérieures non encore déduits (n-5)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5gg(Variable):
    cerfa_field = u"5GG"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus de locations meublées non professionnelles années antérieures non encore déduits (n-4)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5gh(Variable):
    cerfa_field = u"5GH"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus de locations meublées non professionnelles années antérieures non encore déduits (n-3)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5gi(Variable):
    cerfa_field = u"5GI"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus de locations meublées non professionnelles années antérieures non encore déduits (n-2)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5gj(Variable):
    cerfa_field = u"5GJ"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus de locations meublées non professionnelles années antérieures non encore déduits (n-1)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5rn(Variable):
    cerfa_field = u"5RN"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus industriels et commerciaux non professionnelles années antérieures non encore déduits (n-6)"
    start_date = date(2010, 1, 1)
    stop_date = date(2010, 12, 31)



class f5ro(Variable):
    cerfa_field = u"5RO"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus industriels et commerciaux non professionnelles années antérieures non encore déduits (n-5)"



class f5rp(Variable):
    cerfa_field = u"5RP"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus industriels et commerciaux non professionnelles années antérieures non encore déduits (n-4)"



class f5rq(Variable):
    cerfa_field = u"5RQ"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus industriels et commerciaux non professionnelles années antérieures non encore déduits (n-3)"



class f5rr(Variable):
    cerfa_field = u"5RR"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus industriels et commerciaux non professionnelles années antérieures non encore déduits (n-2)"



class f5rw(Variable):
    cerfa_field = u"5RW"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus industriels et commerciaux non professionnelles années antérieures non encore déduits (n-1)"



class f5ht(Variable):
    cerfa_field = u"5HT"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus non commerciaux non professionnelles années antérieures non encore déduits (n-6)"
    start_date = date(2007, 1, 1)



class f5it(Variable):
    cerfa_field = u"5IT"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus non commerciaux non professionnelles années antérieures non encore déduits (n-5)"
    start_date = date(2007, 1, 1)



class f5jt(Variable):
    cerfa_field = u"5JT"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus non commerciaux non professionnelles années antérieures non encore déduits (n-4)"
    start_date = date(2007, 1, 1)



class f5kt(Variable):
    cerfa_field = u"5KT"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus non commerciaux non professionnelles années antérieures non encore déduits (n-3)"
    start_date = date(2007, 1, 1)



class f5lt(Variable):
    cerfa_field = u"5LT"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus non commerciaux non professionnelles années antérieures non encore déduits (n-2)"
    start_date = date(2007, 1, 1)



class f5mt(Variable):
    cerfa_field = u"5MT"
    column = IntCol(val_type = "monetary")
    entity_class = FoyersFiscaux
    label = u"Déficits des revenus non commerciaux non professionnelles années antérieures non encore déduits (n-1)"
    start_date = date(2007, 1, 1)



class f5sq(Variable):
    column = IntCol
    entity_class = Individus




# TODO: Introduit par mes aides à consolider

# Input variables

# Input mensuel
class tns_auto_entrepreneur_chiffre_affaires(Variable):
    column = FloatCol
    entity_class = Individus
    set_input = set_input_divide_by_period
    label = u"Chiffre d'affaires en tant qu'auto-entrepreneur"

# Input annuel
class tns_micro_entreprise_chiffre_affaires(Variable):
    column = FloatCol
    entity_class = Individus
    set_input = set_input_divide_by_period
    label = u"Chiffre d'affaires en de micro-entreprise"

enum_tns_type_activite = Enum([u'achat_revente', u'bic', u'bnc'])


# TODO remove this ugly is_permanent
class tns_auto_entrepreneur_type_activite(Variable):
    column = EnumCol(enum = enum_tns_type_activite)
    entity_class = Individus
    is_permanent = True
    label = u"Type d'activité de l'auto-entrepreneur"

# TODO remove this ugly is_permanent
class tns_micro_entreprise_type_activite(Variable):
    column = EnumCol(enum = enum_tns_type_activite)
    entity_class = Individus
    is_permanent = True
    label = u"Type d'activité de la micro-entreprise"

# Input sur le dernier exercice. Par convention, sur l'année dernière.
class tns_autres_revenus(Variable):
    column = FloatCol
    entity_class = Individus
    set_input = set_input_divide_by_period
    label = u"Autres revenus non salariés"

class tns_autres_revenus_chiffre_affaires(Variable):
    column = FloatCol
    entity_class = Individus
    set_input = set_input_divide_by_period
    label = u"Chiffre d'affaire pour les TNS non agricoles autres que les AE et ME"

class tns_autres_revenus_type_activite(Variable):
    column = EnumCol(enum = enum_tns_type_activite)
    entity_class = Individus
    is_permanent = True
    label = u"Type d'activité de l'entreprise non AE ni ME"

class tns_avec_employe(Variable):
    column = BoolCol
    entity_class = Individus
    set_input = set_input_dispatch_by_period
    label = u"Le TNS a au moins un employé. Ne s'applique pas pour les agricoles ni auto-entrepreneurs ni micro entreprise"

# Input annuel
class tns_benefice_exploitant_agricole(Variable):
    column = FloatCol
    entity_class = Individus
    set_input = set_input_dispatch_by_period
    label = u"Dernier bénéfice agricole"


# Computed variables

class travailleur_non_salarie(Variable):
    label = u"L'individu a une activité professionnelle non salariée"
    column = BoolCol
    entity_class = Individus

    def function(self, simulation, period):
        period = period.this_month
        this_year_and_last_year = period.start.offset('first-of', 'year').period('year', 2).offset(-1)
        tns_auto_entrepreneur_chiffre_affaires = simulation.calculate('tns_auto_entrepreneur_chiffre_affaires', period) != 0
        tns_micro_entreprise_chiffre_affaires = simulation.calculate_add('tns_micro_entreprise_chiffre_affaires', this_year_and_last_year) != 0
        tns_autres_revenus = simulation.calculate_add('tns_autres_revenus', this_year_and_last_year) != 0
        tns_benefice_exploitant_agricole = simulation.calculate_add('tns_benefice_exploitant_agricole', this_year_and_last_year) != 0
        tns_autres_revenus_chiffre_affaires = simulation.calculate_add('tns_autres_revenus_chiffre_affaires', this_year_and_last_year) != 0

        result = (
            tns_auto_entrepreneur_chiffre_affaires + tns_micro_entreprise_chiffre_affaires +
            tns_autres_revenus + tns_benefice_exploitant_agricole + tns_autres_revenus_chiffre_affaires
        )

        return period, result


# Auxiliary function
def compute_benefice_auto_entrepreneur_micro_entreprise(bareme, type_activite, chiffre_affaire):
    abatt_fp_me = bareme.micro_entreprise.abattement_forfaitaire_fp
    benefice = chiffre_affaire * (
        1 -
        (type_activite == 0) * abatt_fp_me.achat_revente -
        (type_activite == 1) * abatt_fp_me.bic -
        (type_activite == 2) * abatt_fp_me.bnc)

    return benefice


class tns_auto_entrepreneur_benefice(DatedVariable):
    column = FloatCol
    label = u"Bénéfice en tant qu'auto-entrepreneur"
    entity_class = Individus

    @dated_function(start = date(2008, 1, 1))
    def function(self, simulation, period):
        period = period.this_month
        tns_auto_entrepreneur_type_activite = simulation.calculate('tns_auto_entrepreneur_type_activite', period)
        tns_auto_entrepreneur_chiffre_affaires = simulation.calculate('tns_auto_entrepreneur_chiffre_affaires', period)
        bareme = simulation.legislation_at(period.start).tns

        benefice = compute_benefice_auto_entrepreneur_micro_entreprise(
            bareme, tns_auto_entrepreneur_type_activite, tns_auto_entrepreneur_chiffre_affaires)
        return period, benefice


class tns_micro_entreprise_benefice(DatedVariable):
    column = FloatCol
    label = u"Bénéfice de la micro entreprise"
    entity_class = Individus

    @dated_function(start = date(2008, 1, 1))
    def function(self, simulation, period):
        period = period.this_year
        tns_micro_entreprise_type_activite = simulation.calculate('tns_micro_entreprise_type_activite', period)
        tns_micro_entreprise_chiffre_affaires = simulation.calculate('tns_micro_entreprise_chiffre_affaires', period)
        bareme = simulation.legislation_at(period.start).tns

        benefice = compute_benefice_auto_entrepreneur_micro_entreprise(
            bareme, tns_micro_entreprise_type_activite, tns_micro_entreprise_chiffre_affaires)
        return period, benefice

# The following formulas take into account 'cotisation sociales'. However, it seems that for all prestations,
# the 'base ressources' are only using the 'benefice', without deducting the 'cotisation sociales'.
# Although this rule seems unfair towards independent workers, we are now applying it for all presations and therefore
# we are not using the following formulas for calculating prestations.
class tns_auto_entrepreneur_revenus_net(DatedVariable) :
    column = FloatCol
    label = u"Revenu d'un auto-entrepreneur"
    entity_class = Individus

    @dated_function(start = date(2008, 1, 1))
    def function(self, simulation, period):
        period = period.this_month
        tns_auto_entrepreneur_benefice = simulation.calculate('tns_auto_entrepreneur_benefice', period)
        tns_auto_entrepreneur_type_activite = simulation.calculate('tns_auto_entrepreneur_type_activite', period)
        tns_auto_entrepreneur_chiffre_affaires = simulation.calculate('tns_auto_entrepreneur_chiffre_affaires', period)
        bareme_cs_ae = simulation.legislation_at(period.start).tns.auto_entrepreneur
        taux_cotisations_sociales_sur_CA = (
            (tns_auto_entrepreneur_type_activite == 0) * bareme_cs_ae.achat_revente +
            (tns_auto_entrepreneur_type_activite == 1) * bareme_cs_ae.bic +
            (tns_auto_entrepreneur_type_activite == 2) * bareme_cs_ae.bnc)
        tns_auto_entrepreneur_charges_sociales = taux_cotisations_sociales_sur_CA * tns_auto_entrepreneur_chiffre_affaires
        revenus = tns_auto_entrepreneur_benefice - tns_auto_entrepreneur_charges_sociales

        return period, revenus


class tns_micro_entreprise_revenus_net(Variable) :
    column = FloatCol
    label = u"Revenu d'un TNS dans une micro-entreprise"
    entity_class = Individus

    def function(self, simulation, period):
        period = period.this_month
        tns_micro_entreprise_benefice = simulation.calculate('tns_micro_entreprise_benefice', period)
        taux_cotisations_sociales = simulation.legislation_at(period.start).tns.micro_entreprise.cotisations_sociales
        tns_micro_entreprise_charges_sociales = tns_micro_entreprise_benefice * taux_cotisations_sociales
        revenus = tns_micro_entreprise_benefice - tns_micro_entreprise_charges_sociales

        return period, revenus

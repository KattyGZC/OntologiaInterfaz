# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.core import serializers
from django.template.loader import render_to_string

from owlready2 import *
from rdflib import *
import json

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Índice'
        
        return context

    def post(self, request, *args, **kwargs):
        
        default_onto = World()
        default_onto.get_ontology("file://E:/HD anterior/OneDrive/ESPE/Noveno Semestre/Tópicos de software/OntologiaAcceso/OntologiaInterfaz/AccesoUNE.owl").load()
        graph = default_onto.as_rdflib_graph()
        qs = ''
        op = ''
        if request.method == 'POST':
            for key, value in request.POST.items():
                op = value
            if op == '1':
                qs = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX au: <http://www.semanticweb.org/labprocesos/ontologies/2021/2/ontologia-une#>

                    SELECT ?Cupo ?Aspirante
                    WHERE {
                    ?cp au:esAsignado ?asp .
                    ?asp au:nombre ?Aspirante .
                    ?cp au:carrera ?Cupo 
                } """
            elif op == '2':
                qs = """ PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX au: <http://www.semanticweb.org/labprocesos/ontologies/2021/2/ontologia-une#>

                    SELECT ?Aspirante ?Examen
                        WHERE { ?a  au:rindeUn ?ptj  .
                                ?a au:nombre ?Aspirante .
                                ?ptj au:puntaje ?Examen 
                } """
            
            elif op == '3':
                qs = """ PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX au: <http://www.semanticweb.org/labprocesos/ontologies/2021/2/ontologia-une#>

                    SELECT ?Inscripcion ?CentroRegulacion
                        WHERE { ?i au:seRegistraEn ?cr .
                                ?i au:codigo ?Inscripcion .
                                ?cr au:nombre ?CentroRegulacion }
                """
            elif op == '4':
                qs = """ PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX au: <http://www.semanticweb.org/labprocesos/ontologies/2021/2/ontologia-une#>

                    SELECT ?Aspirante ?Fecha
                        WHERE { ?a au:rindeUn ?exm .
                                ?a au:nombre ?Aspirante .
                                ?exm au:fecha ?Fecha }
                """
            
            elif op == '5':
                qs = """ PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX au: <http://www.semanticweb.org/labprocesos/ontologies/2021/2/ontologia-une#>

                    SELECT ?Postulacion ?Aspirante
                        WHERE { ?p au:esRealizadaPor ?a .
                                ?p au:fecha_inicio ?Postulacion .
                                ?a au:nombre ?Aspirante }
                """
            
            elif op == '6':
                                    qs = """ PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX au: <http://www.semanticweb.org/labprocesos/ontologies/2021/2/ontologia-une#>

                    SELECT ?Postulacion ?Aspirante
                        WHERE { ?p au:esRealizadaPor ?a .
                                ?p au:fecha_fin ?Postulacion .
                                ?a au:nombre ?Aspirante }
                """
                
            elif op == '7':
                qs = """ PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX au: <http://www.semanticweb.org/labprocesos/ontologies/2021/2/ontologia-une#>

                    SELECT ?Aspirante ?Inscripcion
                        WHERE { ?a au:realizaLa ?i .
                                ?a au:nombre ?Aspirante .
                                ?i au:fecha_inicio ?Inscripcion }
                """

            elif op == '8':
                qs = """ PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX au: <http://www.semanticweb.org/labprocesos/ontologies/2021/2/ontologia-une#>

                    SELECT ?Carrera ?Universidad
                        WHERE { ?c au:esOfertaPor ?u .
                                ?c au:nombre ?Carrera .
                                ?u au:nombre ?Universidad }
                """

            elif op == '9':
                qs = """ PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX owl: <http://www.w3.org/2002/07/owl#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
                    PREFIX au: <http://www.semanticweb.org/labprocesos/ontologies/2021/2/ontologia-une#>

                    SELECT ?Carrera ?Cupo
                        WHERE { ?cr au:ofrecenVarios ?cp .
                                ?cp  au:carrera ?Cupo .
		                        ?cr au:num_aspirantes ?Carrera }
                """
            else:
                return HttpResponse('Sin valor')

            result = (graph.query(qs))
            qresult = []
            for res in result:
                res1 = str(res)
                res2 = res1.replace('rdflib.term.Literal', '')
                res2 = res2.replace(", datatype=rdflib.term.URIRef('http://www.w3.org/2001/XMLSchema#integer'", '')
                qresult.append(res2)
            qres = f'{qresult}'
            
        return HttpResponse(qres, 'application/javascript')

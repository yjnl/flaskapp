FROM python:2-onbuild
COPY *.py /home/
COPY templates/*.* /home/templates/
ENTRYPOINT ["python"]
CMD ["/home/register.py" ]
EXPOSE 5000
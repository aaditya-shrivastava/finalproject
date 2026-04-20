#!/bin/sh

streamlit run manufacturing-creator/app.py --server.port=8500 --server.address=0.0.0.0 &

streamlit run multi-agent-manufacturing/app.py --server.port=8501 --server.address=0.0.0.0 &

streamlit run app.py --server.port=8502 --server.address=0.0.0.0
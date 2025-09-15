all: 
	clear 
# 	python src/main.py --config=cgmix --env-config=gather with seed=100 use_cuda=False 
# 	python src/main.py --config=cgmix --env-config=hallway with seed=100 use_cuda=False 
	python src/main.py --config=cgmix --env-config=disperse with seed=100 use_cuda=False 
# 	python src/main.py --config=cgmix --env-config=pursuit with seed=100 use_cuda=False 
# export PYTHONPATH=$PYTHONPATH:/nfs/kun2/users/asap7772/antmaze_gen
import gym
import d4rl

for val in ['biased', 'noisy']:
    for size in ['medium', 'large']:
        env_name = f'antmaze-{size}-{val}-v2'
        print('Loading', env_name)

        env = gym.make(env_name)
        data = env.get_dataset()
        print(f'Loaded {env_name} with {len(data["observations"])} transitions')

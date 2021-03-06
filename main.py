import gym

from core.trainer import Trainer
from utils.preprocess import greyscale
from utils.wrappers import PreproWrapper, MaxAndSkipEnv

from core.schedule import ExplorationSchedule

from config import Config

if __name__ == "__main__":
    config = Config

    env = gym.make(config.env_name)
    env = MaxAndSkipEnv(env, skip=config.skip_frame)
    env = PreproWrapper(
        env,
        prepro=greyscale,
        shape=(80, 80, 1),
    )

    exp_schedule = ExplorationSchedule(
        env, config.epsilon_init, config.epsilon_final, config.epsilon_interp_limit
    )

    trainer = Trainer(env, config)
    trainer.run(exp_schedule)

# -*- coding: utf-8 -*-

import tensorflow as tf


def get_options():
    tf.app.flags.DEFINE_string('f', '', 'kernel')
    tf.app.flags.DEFINE_string("save_dir", "saved", "checkpoints, log, etc")
    tf.app.flags.DEFINE_string("run_ID", "seq_10_batch_100_RNN_256_nonneg_1e5_DOG_rf_1_no_l2_noclip", "save_ID")
    tf.app.flags.DEFINE_string("train_or_test", "train", "train mode or test mode")
    tf.app.flags.DEFINE_integer("batch_size", 100, "batch size")
    tf.app.flags.DEFINE_integer("sequence_length", 10, "sequence length")
    tf.app.flags.DEFINE_integer("steps", 30000000, "training steps")
    tf.app.flags.DEFINE_integer("save_interval", 1000, "saving interval")
    tf.app.flags.DEFINE_float("keep_prob", 0.5, "dropout rate")
    tf.app.flags.DEFINE_float("learning_rate", 1e-4, "learning rate")
    tf.app.flags.DEFINE_float("l2_reg", 0, "weight decay")
    tf.app.flags.DEFINE_float("gradient_clipping", 1, "gradient clipping")
    tf.app.flags.DEFINE_integer("num_place_cells", 256, "number place cells")
    tf.app.flags.DEFINE_float("place_cell_rf", 0.09, "receptive field")
    tf.app.flags.DEFINE_integer("num_hd_cells", 12, "number hd cells")
    tf.app.flags.DEFINE_float("hd_cell_rf", 20., "hd cell receptive field")
    tf.app.flags.DEFINE_string("RNN_type", "RNN", "recurrent cell type")
    tf.app.flags.DEFINE_float("nonneg_obj", 1e-5, "strength nonnegativity constraint")
    tf.app.flags.DEFINE_bool("meta", False, "perform meta-learning")
    tf.app.flags.DEFINE_bool("place_outputs", True, "train on place cell outputs")
    tf.app.flags.DEFINE_bool("hd_integration", False, "perform hd integration")
    tf.app.flags.DEFINE_bool("DOG", True, "difference of gaussians")
    tf.app.flags.DEFINE_bool("dense_layer", False, "include dense layer g")
    tf.app.flags.DEFINE_integer("num_g_cells", 256, "num grid cells")
    tf.app.flags.DEFINE_integer("rnn_size", 256, "num units in RNN")
    tf.app.flags.DEFINE_float("env_size", 1.1, "environment size")
    tf.app.flags.DEFINE_string("dataset", 'ben_10_step_periodic', "dataset location")
    return tf.app.flags.FLAGS

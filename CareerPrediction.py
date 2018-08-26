{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unindent does not match any outer indentation level (<tokenize>, line 8)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<tokenize>\"\u001b[1;36m, line \u001b[1;32m8\u001b[0m\n\u001b[1;33m    dataset.append(row)\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unindent does not match any outer indentation level\n"
     ]
    }
   ],
   "source": [
    "def load_csv(filename):\n",
    "    dataset = list()\n",
    "    with open(filename, 'r') as file:\n",
    "         csv_reader = reader(file)\n",
    "            for row in csv_reader:\n",
    "                 if not row:\n",
    "                    continue\n",
    "                dataset.append(row)\n",
    "return dataset\n",
    "\n",
    "\n",
    "def str_column_to_float(dataset, column):\n",
    "    for row in dataset:\n",
    "        row[column] = float(row[column].strip())\n",
    "        \n",
    "        \n",
    "def train_test_split(dataset, split):\n",
    "    train = list()\n",
    "    train_size = split * len(dataset)\n",
    "    dataset_copy = list(dataset)\n",
    "    while len(train) < train_test :\n",
    "        index = randrange(len(dataset_copy))\n",
    "        train.append(dataset_copy.pop(index))\n",
    "return train, dataset_copy\n",
    "\n",
    "\n",
    "\n",
    "filename = 'careerdataset.csv'\n",
    "dataset = load_csv(filename)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from random import seed\n",
    "from random import randrange\n",
    "from csv import reader\n",
    "from math import sqrt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

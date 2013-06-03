# |  seek(...)
# |      seek(offset[, whence]) -> None.  Move to new file position.
# |      
# |      Argument offset is a byte count.  Optional argument whence defaults to
# |      0 (offset from start of file, offset should be >= 0); other values are 1
# |      (move relative to current position, positive or negative), and 2 (move
# |      relative to end of file, usually negative, although many platforms allow
# |      seeking beyond the end of a file).  If the file is opened in text mode,
# |      only offsets returned by tell() are legal.  Use of other offsets causes
# |      undefined behavior.
# |      Note that not all file objects are seekable.
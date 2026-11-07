#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2016 The CyanogenMod Project
# SPDX-FileCopyrightText: 2017-2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/miuicamera-everpal',
]

blob_fixups: blob_fixups_user_type = {
    'system/lib64/libcamera_algoup_jni.xiaomi.so': blob_fixup()
            .add_needed('libgui_shim_miuicamera.so')
            .sig_replace('08 AD 40 F9', '08 A9 40 F9'),
    'system/lib64/libcamera_mianode_jni.xiaomi.so': blob_fixup()
            .add_needed('libgui_shim_miuicamera.so'),
    'system/lib64/libcamera_ispinterface_jni.xiaomi.so': blob_fixup()
            .add_needed('libgui_shim_miuicamera.so')
            .remove_needed('libhidltransport.so'),
}

module = ExtractUtilsModule(
    'miuicamera-everpal',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
